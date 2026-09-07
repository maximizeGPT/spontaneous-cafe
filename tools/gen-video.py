#!/usr/bin/env python3
"""Generate the five hero loops with fal.ai (MiniMax Hailuo 02 image-to-video).
Ambience only: motion added to the existing placeholder photos, never a dish invented.
Usage: FAL_KEY=... python3 tools/gen-video.py [shot ...]   (default: all)
Writes raw clips to tools/out/<shot>.raw.mp4. Transcode with tools/place-video.sh.
"""
import json, os, sys, time, urllib.request, concurrent.futures as cf

KEY = os.environ.get('FAL_KEY') or sys.exit('FAL_KEY missing')
BASE = 'https://spontaneous-cafe.vercel.app/assets/img/'
HAILUO = 'https://queue.fal.run/fal-ai/minimax/hailuo-02/standard/image-to-video'
OUT = os.path.join(os.path.dirname(__file__), 'out'); os.makedirs(OUT, exist_ok=True)

SHOTS = {
  'home-pan': ('pan.jpg', "Slow steady handheld shot. Flames flicker under the pan, the food sizzles and light steam rises. The hands hold the pan still and tilt it gently. Warm kitchen light, shallow depth of field, realistic, no text, no new objects."),
  'foraging-moss': ('svc-foraging.jpg', "Locked-off close shot of a basket of wild mushrooms on the forest floor. A gentle breeze moves the ferns and leaves, dappled light shifts slowly, camera drifts forward a little. Natural, realistic, no text, no new objects."),
  'chef-plating': ('svc-chef.jpg', "The chef's hands stay low over the plate the whole time, placing small leaves with tweezers, one at a time, slowly and precisely. The hands never lift above the plate. Very subtle slow push-in. Soft window light, realistic, no text, no new objects."),
  'catering-table': ('table-set.jpg', "Slow dolly forward along a long candlelit dinner table. Candle flames flicker, string lights glow softly, glasses catch the light. No people appear. Warm, realistic, no text, no new objects."),
  'classes-knife': ('knife.jpg', "Hands chop fresh herbs on a wooden board with a chef's knife in a steady rhythm, herbs gather into a pile. Slight handheld movement. Bright home kitchen, realistic, no text, no new objects."),
}

def call(url, data=None, method=None):
    req = urllib.request.Request(url, data=json.dumps(data).encode() if data is not None else None, method=method)
    req.add_header('Authorization', 'Key ' + KEY)
    req.add_header('Content-Type', 'application/json')
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())

def run(shot):
    img, prompt = SHOTS[shot]
    sub = call(HAILUO, {'image_url': BASE + img, 'prompt': prompt, 'duration': 6, 'resolution': '768P', 'prompt_optimizer': True})
    print(shot, 'queued', sub.get('request_id'), flush=True)
    t0 = time.time()
    while True:
        st = call(sub['status_url'])
        if st.get('status') == 'COMPLETED': break
        if st.get('status') not in ('IN_QUEUE', 'IN_PROGRESS'): raise RuntimeError(f'{shot}: {st}')
        if time.time() - t0 > 900: raise RuntimeError(f'{shot}: timeout')
        time.sleep(8)
    res = call(sub['response_url'])
    vurl = (res.get('video') or {}).get('url') or res.get('video_url')
    if not vurl: raise RuntimeError(f'{shot}: no video url in {json.dumps(res)[:400]}')
    path = os.path.join(OUT, shot + '.raw.mp4')
    urllib.request.urlretrieve(vurl, path)
    print(shot, 'done', os.path.getsize(path) // 1024, 'KB in', int(time.time() - t0), 's', flush=True)
    return shot

if __name__ == '__main__':
    shots = sys.argv[1:] or list(SHOTS)
    with cf.ThreadPoolExecutor(max_workers=5) as ex:
        for f in cf.as_completed([ex.submit(run, s) for s in shots]):
            try: f.result()
            except Exception as e: print('ERROR', e, flush=True)

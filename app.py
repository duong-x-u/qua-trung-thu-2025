from flask import Flask, render_template_string, jsonify, url_for
import random
from datetime import datetime, timezone

app = Flask(__name__)

START_DATE = datetime(2025, 7, 23, tzinfo=timezone.utc)
WISHES = ["Trung Thu rùi, mún ngắm trăng cùng Trà My quó òoo🌕💕", "Bánh Trung Thu ngọt đến mấy cũng không bằng nụ cười của My :333 🥮😊", "Chúc My Trung Thu zui zẻ nhooooooooooooooooooooo", "Iu gái quá >.< ", "Xa nhau mà vẫn nhớ My từng giây từng phút 🥺💕", "My là ánh trăng đẹp nhất trong đời anh 🌙✨", "Mong sao Trung Thu này mình được ở bên nhau nha 💑", "Dù cách xa mấy cũng không làm anh bớt yêu em đâu 💖"]

# DANH SÁCH TÊN FILE NHẠC TRONG THƯ MỤC ASSETS
MUSIC_FILES = [
    'btyl-rm.mp3',
    'cđôt.mp3',
    'btyl.mp3'
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Qùa cho PÉ EWWWWWWW 🥮💕</title>
    <style>
        /* Toàn bộ CSS của bạn, không đổi */
        @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;600;700&display=swap');
        body{font-family:'Quicksand',sans-serif;background:linear-gradient(135deg,#1a1a2e 0%,#16213e 50%,#0f3460 100%);min-height:100vh;padding:40px 20px;position:relative;overflow-x:hidden;overflow-y:auto;cursor:default}*{margin:0;padding:0;box-sizing:border-box}.moon{position:fixed;top:8%;right:12%;width:180px;height:180px;background:radial-gradient(circle at 35% 35%,#fff9e6,#ffd700);border-radius:50%;box-shadow:0 0 100px rgba(255,215,0,.5),0 0 200px rgba(255,215,0,.3),inset -25px -25px 50px rgba(0,0,0,.1);animation:moonGlow 4s ease-in-out infinite;z-index:1;pointer-events:none}@keyframes moonGlow{0%,100%{box-shadow:0 0 100px rgba(255,215,0,.5),0 0 200px rgba(255,215,0,.3),inset -25px -25px 50px rgba(0,0,0,.1)}50%{box-shadow:0 0 140px rgba(255,215,0,.7),0 0 250px rgba(255,215,0,.4),inset -25px -25px 50px rgba(0,0,0,.1)}}.shooting-star{position:fixed;width:2px;height:2px;background:white;border-radius:50%;box-shadow:0 0 10px white;animation:shoot linear;pointer-events:none}@keyframes shoot{0%{transform:translate(0,0) rotate(-45deg);opacity:1}100%{transform:translate(-300px,300px) rotate(-45deg);opacity:0}}.shooting-star::after{content:'';position:absolute;top:0;left:0;width:60px;height:1px;background:linear-gradient(to right,white,transparent)}.star{position:fixed;background:white;border-radius:50%;animation:twinkle ease-in-out infinite;pointer-events:none}@keyframes twinkle{0%,100%{opacity:.2;transform:scale(1)}50%{opacity:1;transform:scale(1.3)}}.click-heart{position:fixed;font-size:30px;pointer-events:none;animation:heartFloat 2s ease-out forwards;z-index:9999}@keyframes heartFloat{0%{transform:translateY(0) scale(.5) rotate(0deg);opacity:1}100%{transform:translateY(-200px) scale(1.5) rotate(360deg);opacity:0}}.click-ripple{position:fixed;border:3px solid;border-radius:50%;pointer-events:none;animation:ripple 1s ease-out forwards;z-index:9999}@keyframes ripple{0%{width:0;height:0;opacity:1}100%{width:150px;height:150px;opacity:0}}.click-particle{position:fixed;width:8px;height:8px;border-radius:50%;pointer-events:none;animation:particle 1.5s ease-out forwards;z-index:9999}@keyframes particle{0%{transform:translate(0,0) scale(1);opacity:1}100%{transform:translate(var(--tx),var(--ty)) scale(0);opacity:0}}.container{background:linear-gradient(135deg,rgba(255,255,255,.98) 0%,rgba(255,250,240,.98) 100%);border-radius:30px;padding:50px 40px;max-width:650px;width:100%;margin:0 auto;box-shadow:0 25px 80px rgba(0,0,0,.4),0 0 100px rgba(255,107,157,.2);position:relative;z-index:10;animation:fadeInUp 1.2s ease;border:2px solid transparent;background-clip:padding-box}.container::before{content:'';position:absolute;top:-2px;left:-2px;right:-2px;bottom:-2px;background:linear-gradient(45deg,#ff6b9d,#ffd700,#ff6b9d,#ffd700);border-radius:30px;z-index:-1;animation:borderRotate 3s linear infinite;background-size:300% 300%}@keyframes borderRotate{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}@keyframes fadeInUp{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:translateY(0)}}h1{background:linear-gradient(135deg,#ff6b9d,#ffd700,#ff6b9d);background-size:200% 200%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;font-size:2.5em;margin-bottom:10px;text-align:center;font-weight:800;letter-spacing:1px;animation:gradientShift 3s ease infinite;font-family:'Pacifico',cursive;cursor:pointer}@keyframes gradientShift{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}#main-title>span{display:inline-block;transition:transform .3s cubic-bezier(.25,.46,.45,.94)}#main-title:hover>span{transform:translateY(-10px) scale(1.1)}.subtitle{color:#8e44ad;font-size:1.2em;margin-bottom:20px;font-style:italic;text-align:center;opacity:.9}.love-counter{background:linear-gradient(135deg,#ff6b9d22,#ffd70022);border:2px solid #ff6b9d;border-radius:20px;padding:20px;margin:25px 0;text-align:center;position:relative;overflow:hidden}.love-counter::before{content:'💕';position:absolute;font-size:60px;opacity:.1;top:50%;left:50%;transform:translate(-50%,-50%);animation:heartPulse 3s ease-in-out infinite}@keyframes heartPulse{0%,100%{transform:translate(-50%,-50%) scale(1)}50%{transform:translate(-50%,-50%) scale(1.2)}}.love-counter-label{font-size:1.1em;color:#c2185b;font-weight:600;margin-bottom:8px}.love-counter-days{font-size:3em;font-weight:800;background:linear-gradient(135deg,#e91e63,#ff6b9d);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;font-family:'Pacifico',cursive;position:relative;z-index:1}.love-counter-text{font-size:1em;color:#880e4f;font-weight:600;margin-top:5px}.mooncake-container{display:flex;justify-content:center;margin:35px 0}.mooncake{width:220px;height:220px;position:relative;animation:float 4s ease-in-out infinite;filter:drop-shadow(0 15px 30px rgba(243,156,18,.4));cursor:pointer;transition:transform .2s ease}.mooncake:hover{transform:scale(1.05);animation-play-state:paused}.mooncake:active{transform:scale(.95)}@keyframes float{0%,100%{transform:translateY(0) rotate(0deg)}25%{transform:translateY(-20px) rotate(3deg)}50%{transform:translateY(0) rotate(0deg)}75%{transform:translateY(-20px) rotate(-3deg)}}.mooncake svg{width:100%;height:100%;animation:rotateCake 30s linear infinite}@keyframes rotateCake{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}.mooncake::before{content:'';position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:260px;height:260px;border-radius:50%;background:radial-gradient(circle,rgba(255,215,0,.2),transparent);animation:pulseGlow 2s ease-in-out infinite;pointer-events:none}@keyframes pulseGlow{0%,100%{transform:translate(-50%,-50%) scale(1);opacity:.4}50%{transform:translate(-50%,-50%) scale(1.15);opacity:.7}}.wish-box{background:linear-gradient(135deg,#fff3e0 0%,#ffe0b2 100%);padding:30px;border-radius:20px;margin:35px 0;border:2px solid #ffb74d;position:relative;box-shadow:0 8px 25px rgba(255,152,0,.2)}.wish-box::before,.wish-box::after{content:'💝';position:absolute;font-size:26px;opacity:.35;animation:heartBeat 2s ease-in-out infinite}@keyframes heartBeat{0%,100%{transform:scale(1)}50%{transform:scale(1.15)}}.wish-box::before{top:12px;left:12px}.wish-box::after{bottom:12px;right:12px;animation-delay:1s}.wish-text{font-size:1.3em;color:#6d4c41;line-height:1.7;font-weight:500;text-align:center;position:relative;z-index:1;transition:all .5s ease}.wish-text.changing{opacity:0;transform:translateY(-10px)}.countdown{margin-top:25px;text-align:center;color:#5e35b1;font-size:1em;display:flex;align-items:center;justify-content:center;gap:12px;opacity:.9}.timer-circle{width:50px;height:50px;border-radius:50%;background:linear-gradient(135deg,#7e57c2,#5e35b1);display:flex;align-items:center;justify-content:center;color:white;font-size:1.3em;font-weight:600;box-shadow:0 5px 15px rgba(94,53,177,.3);animation:timerPulse 1s ease-in-out infinite}@keyframes timerPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.08)}}.footer-message{margin-top:35px;text-align:center;background:linear-gradient(135deg,#e91e63,#ff6b9d);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;font-size:1.25em;font-weight:700;letter-spacing:.5px}.divider{height:2px;background:linear-gradient(to right,transparent,#e0e0e0,transparent);margin:30px 0}#drawCanvas{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:9998}.confetti{position:fixed;width:10px;height:10px;pointer-events:none;animation:confettiFall linear forwards;z-index:9999}@keyframes confettiFall{0%{transform:translateY(0) rotateZ(0deg);opacity:1}100%{transform:translateY(100vh) rotateZ(720deg);opacity:0}}.lantern{position:fixed;bottom:-200px;width:100px;height:150px;background-image:url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 150"><ellipse cx="50" cy="75" rx="45" ry="65" fill="%23d32f2f"/><rect x="40" y="0" width="20" height="15" fill="%23795548"/><rect x="45" y="140" width="10" height="10" fill="%23f9a825"/><path d="M45,145 l-5,10 h20 l-5,-10 z" fill="%23e65100" opacity="0.8"/><circle cx="50" cy="75" r="15" fill="rgba(255,235,59,0.8)" filter="url(%23glow)"/><defs><filter id="glow"><feGaussianBlur stdDeviation="3.5" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs></svg>');background-size:contain;background-repeat:no-repeat;animation:floatUp linear infinite;z-index:5;opacity:.7}@keyframes floatUp{0%{bottom:-200px;transform:translateX(0) rotate(-5deg)}50%{transform:translateX(20px) rotate(5deg)}100%{bottom:110vh;transform:translateX(-20px) rotate(-5deg)}}@media (max-width:600px){body{padding:20px 15px}.container{padding:35px 25px}h1{font-size:2em}.subtitle{font-size:1.1em}.love-counter-days{font-size:2.5em}.mooncake{width:170px;height:170px}.wish-text{font-size:1.15em}.moon{width:120px;height:120px;top:5%;right:5%}.footer-message{font-size:1.1em}.lantern{width:60px;height:90px}}
    </style>
</head>
<body>
    <audio id="backgroundMusic" loop></audio>
    <div class="lantern" style="left: 15%; animation-duration: 20s;"></div>
    <div class="lantern" style="left: 40%; animation-duration: 25s; animation-delay: 5s;"></div>
    <div class="lantern" style="left: 70%; animation-duration: 18s; animation-delay: 2s;"></div>
    <canvas id="drawCanvas"></canvas>
    <div class="moon"></div>
    
    <!-- === PHẦN LOGIC TÌNH YÊU TRUNG THU ĐÃ ĐƯỢC TRẢ LẠI ĐÂY === -->
    <div class="container">
        <h1 id="main-title">🥮 Quà Trung Thu 🥮</h1>
        <p class="subtitle">Trung Thu zui zẻ nhoaaaaaaa (❁´◡`❁)</p>
        <div class="love-counter">
            <p class="love-counter-label">Mình đã bên nhau</p>
            <p class="love-counter-days" id="loveDays">...</p>
            <p class="love-counter-text">ngày rùi đó!</p>
        </div>
        <div class="divider"></div>
        <div class="mooncake-container">
            <div class="mooncake" id="mooncake" onclick="drawName(event)">
                <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="100" cy="100" r="80" fill="#f39c12" stroke="#d68910" stroke-width="3"/>
                    <circle cx="100" cy="100" r="80" fill="none" stroke="#8b4513" stroke-width="2" stroke-dasharray="5,5"/>
                    <circle cx="100" cy="100" r="50" fill="#e67e22" stroke="#d68910" stroke-width="2"/>
                    <text x="100" y="115" font-size="26" fill="#8b4513" text-anchor="middle" font-weight="bold">愛</text>
                    <circle cx="100" cy="40" r="5" fill="#8b4513"/><circle cx="100" cy="160" r="5" fill="#8b4513"/>
                    <circle cx="40" cy="100" r="5" fill="#8b4513"/><circle cx="160" cy="100" r="5" fill="#8b4513"/>
                    <circle cx="60" cy="60" r="4" fill="#8b4513"/><circle cx="140" cy="60" r="4" fill="#8b4513"/>
                    <circle cx="60" cy="140" r="4" fill="#8b4513"/><circle cx="140" cy="140" r="4" fill="#8b4513"/>
                </svg>
            </div>
        </div>
        <div class="divider"></div>
        <div class="wish-box">
            <p class="wish-text" id="wishText">{{ wish }}</p>
        </div>
        <div class="countdown">
            <span>Câu chúc mới sau</span>
            <div class="timer-circle" id="countdown">10</div>
            <span>giây</span>
        </div>
        <div class="divider"></div>
        <p class="footer-message">Yêu em nhiều nhất trên đời! 💕</p>
    </div>
    
    <script>
        const music = document.getElementById('backgroundMusic');
        let musicCanPlay = false;

        document.addEventListener('DOMContentLoaded', () => {
            const musicPath = `{{ url_for('static', filename='assets/' + music_file) }}`;
            music.src = musicPath;
            music.volume = 0.3;

            music.addEventListener('canplaythrough', () => {
                musicCanPlay = true;
                console.log("Music is ready. Waiting for user interaction.");
            });
            
            // Lắng nghe click để phát nhạc, chỉ chạy 1 lần
            document.body.addEventListener('click', () => {
                if (musicCanPlay && music.paused) {
                    music.play().catch(e => console.error("Error playing music:", e));
                }
            }, { once: true });

            getLoveDays();
            countdownInterval = setInterval(updateCountdown, 1000);
        });

        // --- CÁC HÀM CŨ CỦA BẠN (hiệu ứng, countdown, getLoveDays, v.v...) ---
        document.addEventListener('mousemove', function(e) { let body = document.querySelector('body'); let sparkle = document.createElement('span'); sparkle.style.position = 'absolute'; sparkle.style.left = e.pageX + 'px'; sparkle.style.top = e.pageY + 'px'; let size = Math.random() * 8; sparkle.style.width = 2 + size + 'px'; sparkle.style.height = 2 + size + 'px'; sparkle.style.background = `radial-gradient(circle, #ffd700, transparent)`; sparkle.style.borderRadius = '50%'; sparkle.style.pointerEvents = 'none'; sparkle.style.zIndex = '9999'; sparkle.style.transition = 'all 0.5s ease'; let transformValue = Math.random() * 360; sparkle.style.transform = `rotate(${transformValue}deg)`; body.appendChild(sparkle); setTimeout(() => { sparkle.remove(); }, 1000); });
        const title = document.getElementById('main-title'); const text = title.innerText; title.innerHTML = ''; text.split('').forEach((char, index) => { const span = document.createElement('span'); span.innerText = char; span.style.transitionDelay = `${index * 50}ms`; title.appendChild(span); });
        const canvas = document.getElementById('drawCanvas'); const ctx = canvas.getContext('2d');
        function resizeCanvas() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
        resizeCanvas(); window.addEventListener('resize', resizeCanvas);
        function drawName(e) { e.stopPropagation(); createConfetti(e.clientX, e.clientY); const text = 'iu My :3'; const x = Math.random() * (window.innerWidth - 300) + 150; const y = Math.random() * (window.innerHeight - 200) + 150; ctx.font = 'bold 90px "Pacifico", cursive'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; let progress = 0; const drawInterval = setInterval(() => { progress += 0.03; if (progress >= 1) { clearInterval(drawInterval); setTimeout(() => fadeOutText(x, y, text), 2000); return; } ctx.clearRect(0, 0, canvas.width, canvas.height); const gradient = ctx.createLinearGradient(x - 100, y, x + 100, y); gradient.addColorStop(0, '#ff6b9d'); gradient.addColorStop(0.5, '#ffd700'); gradient.addColorStop(1, '#ff6b9d'); ctx.strokeStyle = '#8b4513'; ctx.lineWidth = 6; ctx.globalAlpha = progress; ctx.strokeText(text, x, y); ctx.fillStyle = gradient; ctx.globalAlpha = progress; ctx.fillText(text, x, y); ctx.globalAlpha = 1; }, 20); }
        function fadeOutText(x, y, text) { let alpha = 1; const fadeInterval = setInterval(() => { alpha -= 0.05; if (alpha <= 0) { clearInterval(fadeInterval); ctx.clearRect(0, 0, canvas.width, canvas.height); return; } ctx.clearRect(0, 0, canvas.width, canvas.height); const gradient = ctx.createLinearGradient(x - 100, y, x + 100, y); gradient.addColorStop(0, '#ff6b9d'); gradient.addColorStop(0.5, '#ffd700'); gradient.addColorStop(1, '#ff6b9d'); ctx.globalAlpha = alpha; ctx.strokeStyle = '#8b4513'; ctx.lineWidth = 6; ctx.strokeText(text, x, y); ctx.fillStyle = gradient; ctx.fillText(text, x, y); ctx.globalAlpha = 1; }, 50); }
        function createConfetti(x, y) { const colors = ['#ff6b9d', '#ffd700', '#ff1744', '#00bcd4', '#9c27b0', '#4caf50']; const shapes = ['💕', '⭐', '🌟', '💖', '✨']; for (let i = 0; i < 30; i++) { const confetti = document.createElement('div'); confetti.className = 'confetti'; confetti.style.left = x + 'px'; confetti.style.top = y + 'px'; confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)]; confetti.style.animationDuration = (Math.random() * 2 + 2) + 's'; confetti.style.animationDelay = (Math.random() * 0.3) + 's'; if (Math.random() > 0.5) { confetti.textContent = shapes[Math.floor(Math.random() * shapes.length)]; confetti.style.backgroundColor = 'transparent'; confetti.style.fontSize = '20px'; } document.body.appendChild(confetti); setTimeout(() => confetti.remove(), 4000); } }
        for (let i = 0; i < 60; i++) { let star = document.createElement('div'); star.className = 'star'; let size = Math.random() * 2.5 + 1; star.style.width = size + 'px'; star.style.height = size + 'px'; star.style.left = Math.random() * 100 + '%'; star.style.top = Math.random() * 100 + '%'; star.style.animationDuration = (Math.random() * 3 + 1.5) + 's'; star.style.animationDelay = Math.random() * 5 + 's'; document.body.appendChild(star); }
        function createShootingStar() { const star = document.createElement('div'); star.className = 'shooting-star'; star.style.left = Math.random() * window.innerWidth + 'px'; star.style.top = Math.random() * (window.innerHeight / 2) + 'px'; star.style.animationDuration = (Math.random() * 1 + 0.8) + 's'; document.body.appendChild(star); setTimeout(() => star.remove(), 1500); } setInterval(createShootingStar, 3000);
        document.addEventListener('click', (e) => { const hearts = ['💕', '💖', '💗', '💝', '💘']; for (let i = 0; i < 3; i++) { setTimeout(() => { const heart = document.createElement('div'); heart.className = 'click-heart'; heart.textContent = hearts[Math.floor(Math.random() * hearts.length)]; heart.style.left = (e.clientX - 15 + Math.random() * 30) + 'px'; heart.style.top = e.clientY + 'px'; document.body.appendChild(heart); setTimeout(() => heart.remove(), 2000); }, i * 150); } const colors = ['#ff6b9d', '#ffd700', '#ff1744', '#00bcd4']; for (let i = 0; i < 2; i++) { setTimeout(() => { const ripple = document.createElement('div'); ripple.className = 'click-ripple'; ripple.style.left = e.clientX + 'px'; ripple.style.top = e.clientY + 'px'; ripple.style.borderColor = colors[Math.floor(Math.random() * colors.length)]; document.body.appendChild(ripple); setTimeout(() => ripple.remove(), 1000); }, i * 100); } for (let i = 0; i < 8; i++) { const particle = document.createElement('div'); particle.className = 'click-particle'; const angle = (i / 8) * Math.PI * 2; const distance = 60 + Math.random() * 30; particle.style.left = e.clientX + 'px'; particle.style.top = e.clientY + 'px'; particle.style.background = colors[Math.floor(Math.random() * colors.length)]; particle.style.setProperty('--tx', Math.cos(angle) * distance + 'px'); particle.style.setProperty('--ty', Math.sin(angle) * distance + 'px'); document.body.appendChild(particle); setTimeout(() => particle.remove(), 1500); } });
        let countdown = 10; let countdownInterval;
        function updateCountdown() { countdown--; document.getElementById('countdown').textContent = countdown; if (countdown <= 0) { getNewWish(); countdown = 10; } }
        function getNewWish() { const wishText = document.getElementById('wishText'); wishText.classList.add('changing'); setTimeout(() => { fetch('/api/wish').then(response => response.json()).then(data => { wishText.textContent = data.wish; wishText.classList.remove('changing'); }); }, 500); }
        function getLoveDays() { fetch('/api/love-days').then(response => response.json()).then(data => { document.getElementById('loveDays').textContent = data.days; }); }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    wish = random.choice(WISHES)
    selected_music_file = random.choice(MUSIC_FILES)
    return render_template_string(HTML_TEMPLATE, wish=wish, music_file=selected_music_file)

@app.route('/api/wish')
def get_wish(): return jsonify({'wish': random.choice(WISHES)})

@app.route('/api/love-days')
def get_love_days():
    now = datetime.now(timezone.utc)
    delta = now - START_DATE
    return jsonify({'days': delta.days})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

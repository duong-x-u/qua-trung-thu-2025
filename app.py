from flask import Flask, render_template_string, send_from_directory
import random
import os

app = Flask(__name__)

# Danh sách câu chúc - Để 2-3 câu, bạn thêm vào sau
WISHES = [
    "Trung Thu rùi, mún ngắm trăng cùng Xù qué òoo🌕💕",
    "Bánh Trung Thu ngọt đến mấy cũng không bằng nụ cười của Xù :333 🥮😊",
    "Chúc Xù Trung Thu zui zẻ nhooooooooooooooooooooo",
    "Iu gái quó >.< "
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Qùa cho PÉ EWWWWWWW 🥮💕</title>
    <style>
        @font-face {
            font-family: 'SVN-Ready';
            src: url('/fonts/SVN-Ready.ttf') format('truetype');
            font-weight: normal;
            font-style: normal;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            min-height: 100vh;
            padding: 40px 20px;
            position: relative;
            overflow-x: hidden;
            overflow-y: auto;
            cursor: default;
        }
        
        /* Hiệu ứng trăng */
        .moon {
            position: fixed;
            top: 8%;
            right: 12%;
            width: 180px;
            height: 180px;
            background: radial-gradient(circle at 35% 35%, #fff9e6, #ffd700);
            border-radius: 50%;
            box-shadow: 0 0 100px rgba(255, 215, 0, 0.5),
                        0 0 200px rgba(255, 215, 0, 0.3),
                        inset -25px -25px 50px rgba(0,0,0,0.1);
            animation: moonGlow 4s ease-in-out infinite;
            z-index: 1;
            pointer-events: none;
        }
        
        @keyframes moonGlow {
            0%, 100% { 
                box-shadow: 0 0 100px rgba(255, 215, 0, 0.5),
                           0 0 200px rgba(255, 215, 0, 0.3),
                           inset -25px -25px 50px rgba(0,0,0,0.1);
            }
            50% { 
                box-shadow: 0 0 140px rgba(255, 215, 0, 0.7),
                           0 0 250px rgba(255, 215, 0, 0.4),
                           inset -25px -25px 50px rgba(0,0,0,0.1);
            }
        }
        
        /* Hiệu ứng sao rơi */
        .shooting-star {
            position: fixed;
            width: 2px;
            height: 2px;
            background: white;
            border-radius: 50%;
            box-shadow: 0 0 10px white;
            animation: shoot linear;
            pointer-events: none;
        }
        
        @keyframes shoot {
            0% {
                transform: translate(0, 0) rotate(-45deg);
                opacity: 1;
            }
            100% {
                transform: translate(-300px, 300px) rotate(-45deg);
                opacity: 0;
            }
        }
        
        .shooting-star::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 60px;
            height: 1px;
            background: linear-gradient(to right, white, transparent);
        }
        
        /* Ngôi sao nhấp nháy */
        .star {
            position: fixed;
            background: white;
            border-radius: 50%;
            animation: twinkle ease-in-out infinite;
            pointer-events: none;
        }
        
        @keyframes twinkle {
            0%, 100% { opacity: 0.2; transform: scale(1); }
            50% { opacity: 1; transform: scale(1.3); }
        }
        
        /* Hiệu ứng click - Vòng tròn lan tỏa */
        .click-ripple {
            position: fixed;
            border: 3px solid;
            border-radius: 50%;
            pointer-events: none;
            animation: ripple 1s ease-out forwards;
            z-index: 9999;
        }
        
        @keyframes ripple {
            0% {
                width: 0;
                height: 0;
                opacity: 1;
            }
            100% {
                width: 150px;
                height: 150px;
                opacity: 0;
            }
        }
        
        /* Hiệu ứng click - Hạt sáng bay */
        .click-particle {
            position: fixed;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            pointer-events: none;
            animation: particle 1.5s ease-out forwards;
            z-index: 9999;
        }
        
        @keyframes particle {
            0% {
                transform: translate(0, 0) scale(1);
                opacity: 1;
            }
            100% {
                transform: translate(var(--tx), var(--ty)) scale(0);
                opacity: 0;
            }
        }
        
        /* Container chính */
        .container {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(255, 250, 240, 0.98) 100%);
            border-radius: 30px;
            padding: 50px 40px;
            max-width: 650px;
            width: 100%;
            margin: 0 auto;
            box-shadow: 0 25px 80px rgba(0,0,0,0.4),
                        0 0 100px rgba(255, 107, 157, 0.2);
            position: relative;
            z-index: 10;
            animation: fadeInUp 1.2s ease;
            border: 2px solid transparent;
            background-clip: padding-box;
        }
        
        .container::before {
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            background: linear-gradient(45deg, #ff6b9d, #ffd700, #ff6b9d, #ffd700);
            border-radius: 30px;
            z-index: -1;
            animation: borderRotate 3s linear infinite;
            background-size: 300% 300%;
        }
        
        @keyframes borderRotate {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(40px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Tiêu đề */
        h1 {
            background: linear-gradient(135deg, #ff6b9d, #ffd700, #ff6b9d);
            background-size: 200% 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-size: 2.5em;
            margin-bottom: 10px;
            text-align: center;
            font-weight: 800;
            letter-spacing: 1px;
            animation: gradientShift 3s ease infinite;
        }
        
        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        .subtitle {
            color: #8e44ad;
            font-size: 1.2em;
            margin-bottom: 35px;
            font-style: italic;
            text-align: center;
            opacity: 0.9;
        }
        
        /* Hình bánh Trung Thu */
        .mooncake-container {
            display: flex;
            justify-content: center;
            margin: 35px 0;
        }
        
        .mooncake {
            width: 220px;
            height: 220px;
            position: relative;
            animation: float 4s ease-in-out infinite;
            filter: drop-shadow(0 15px 30px rgba(243, 156, 18, 0.4));
            cursor: pointer;
            transition: transform 0.2s ease;
        }
        
        .mooncake:hover {
            transform: scale(1.05);
        }
        
        .mooncake:active {
            transform: scale(0.95);
        }
        
        @keyframes float {
            0%, 100% { 
                transform: translateY(0) rotate(0deg);
            }
            25% {
                transform: translateY(-20px) rotate(3deg);
            }
            50% { 
                transform: translateY(0) rotate(0deg);
            }
            75% {
                transform: translateY(-20px) rotate(-3deg);
            }
        }
        
        .mooncake svg {
            width: 100%;
            height: 100%;
            animation: rotateCake 30s linear infinite;
        }
        
        @keyframes rotateCake {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        
        /* Vòng sáng quanh bánh */
        .mooncake::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 260px;
            height: 260px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(255,215,0,0.2), transparent);
            animation: pulseGlow 2s ease-in-out infinite;
            pointer-events: none;
        }
        
        @keyframes pulseGlow {
            0%, 100% { 
                transform: translate(-50%, -50%) scale(1);
                opacity: 0.4;
            }
            50% { 
                transform: translate(-50%, -50%) scale(1.15);
                opacity: 0.7;
            }
        }
        
        /* Câu chúc */
        .wish-box {
            background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
            padding: 30px;
            border-radius: 20px;
            margin: 35px 0;
            border: 2px solid #ffb74d;
            position: relative;
            box-shadow: 0 8px 25px rgba(255, 152, 0, 0.2);
        }
        
        .wish-box::before,
        .wish-box::after {
            content: '💝';
            position: absolute;
            font-size: 26px;
            opacity: 0.35;
            animation: heartBeat 2s ease-in-out infinite;
        }
        
        @keyframes heartBeat {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.15); }
        }
        
        .wish-box::before {
            top: 12px;
            left: 12px;
        }
        
        .wish-box::after {
            bottom: 12px;
            right: 12px;
            animation-delay: 1s;
        }
        
        .wish-text {
            font-size: 1.3em;
            color: #6d4c41;
            line-height: 1.7;
            font-weight: 500;
            text-align: center;
            position: relative;
            z-index: 1;
            transition: all 0.5s ease;
        }
        
        .wish-text.changing {
            opacity: 0;
            transform: translateY(-10px);
        }
        
        /* Countdown timer */
        .countdown {
            margin-top: 25px;
            text-align: center;
            color: #5e35b1;
            font-size: 1em;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            opacity: 0.9;
        }
        
        .timer-circle {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: linear-gradient(135deg, #7e57c2, #5e35b1);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.3em;
            font-weight: 600;
            box-shadow: 0 5px 15px rgba(94, 53, 177, 0.3);
            animation: timerPulse 1s ease-in-out infinite;
        }
        
        @keyframes timerPulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.08); }
        }
        
        /* Thông điệp cuối */
        .footer-message {
            margin-top: 35px;
            text-align: center;
            background: linear-gradient(135deg, #e91e63, #ff6b9d);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-size: 1.25em;
            font-weight: 700;
            letter-spacing: 0.5px;
        }
        
        /* Divider */
        .divider {
            height: 2px;
            background: linear-gradient(to right, transparent, #e0e0e0, transparent);
            margin: 30px 0;
        }
        
        /* Canvas vẽ chữ */
        #drawCanvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 9998;
        }
        
        /* Responsive */
        @media (max-width: 600px) {
            body {
                padding: 20px 15px;
            }
            
            .container {
                padding: 35px 25px;
            }
            
            h1 {
                font-size: 2em;
            }
            
            .subtitle {
                font-size: 1.1em;
            }
            
            .mooncake {
                width: 170px;
                height: 170px;
            }
            
            .wish-text {
                font-size: 1.15em;
            }
            
            .moon {
                width: 120px;
                height: 120px;
                top: 5%;
                right: 5%;
            }
            
            .footer-message {
                font-size: 1.1em;
            }
        }
    </style>
</head>
<body>
    <!-- Canvas để vẽ chữ -->
    <canvas id="drawCanvas"></canvas>
    
    <!-- Trăng -->
    <div class="moon"></div>
    
    <script>
        // Setup canvas
        const canvas = document.getElementById('drawCanvas');
        const ctx = canvas.getContext('2d');
        
        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        
        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);
        
        // Vẽ chữ với hiệu ứng
        function drawName(e) {
            e.stopPropagation();
            
            const text = 'iu xù :3';
            const x = Math.random() * (window.innerWidth - 300) + 150;
            const y = Math.random() * (window.innerHeight - 200) + 150;
            
            // Thiết lập font và style
            ctx.font = 'bold 120px "SVN-Ready", sans-serif';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            
            // Vẽ từng nét chữ với hiệu ứng
            let progress = 0;
            const drawInterval = setInterval(() => {
                progress += 0.02;
                
                if (progress >= 1) {
                    clearInterval(drawInterval);
                    // Sau 2 giây thì fade out
                    setTimeout(() => fadeOutText(x, y, text), 2000);
                    return;
                }
                
                // Clear toàn bộ canvas
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                // Vẽ viền đen (stroke)
                ctx.strokeStyle = '#000000';
                ctx.lineWidth = 8;
                ctx.globalAlpha = progress;
                ctx.strokeText(text, x, y);
                
                // Vẽ chữ trắng bên trong
                ctx.fillStyle = '#FFFFFF';
                ctx.globalAlpha = progress;
                ctx.fillText(text, x, y);
                
                ctx.globalAlpha = 1;
            }, 20);
        }
        
        function fadeOutText(x, y, text) {
            let alpha = 1;
            const fadeInterval = setInterval(() => {
                alpha -= 0.05;
                
                if (alpha <= 0) {
                    clearInterval(fadeInterval);
                    ctx.clearRect(0, 0, canvas.width, canvas.height);
                    return;
                }
                
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                // Vẽ với alpha giảm dần
                ctx.globalAlpha = alpha;
                ctx.strokeStyle = '#000000';
                ctx.lineWidth = 8;
                ctx.strokeText(text, x, y);
                
                ctx.fillStyle = '#FFFFFF';
                ctx.fillText(text, x, y);
                
                ctx.globalAlpha = 1;
            }, 50);
        }
        
        // Tạo ngôi sao nhấp nháy
        for(let i = 0; i < 60; i++) {
            let star = document.createElement('div');
            star.className = 'star';
            let size = Math.random() * 2.5 + 1;
            star.style.width = size + 'px';
            star.style.height = size + 'px';
            star.style.left = Math.random() * 100 + '%';
            star.style.top = Math.random() * 100 + '%';
            star.style.animationDuration = (Math.random() * 3 + 1.5) + 's';
            star.style.animationDelay = Math.random() * 5 + 's';
            document.body.appendChild(star);
        }
        
        // Tạo sao rơi định kỳ
        function createShootingStar() {
            const star = document.createElement('div');
            star.className = 'shooting-star';
            star.style.left = Math.random() * window.innerWidth + 'px';
            star.style.top = Math.random() * (window.innerHeight / 2) + 'px';
            star.style.animationDuration = (Math.random() * 1 + 0.8) + 's';
            document.body.appendChild(star);
            
            setTimeout(() => star.remove(), 1500);
        }
        
        setInterval(createShootingStar, 3000);
        
        // Hiệu ứng click - Vòng tròn + hạt sáng
        document.addEventListener('click', (e) => {
            // Tạo vòng tròn lan tỏa
            const colors = ['#ff6b9d', '#ffd700', '#ff1744', '#00bcd4'];
            for(let i = 0; i < 3; i++) {
                setTimeout(() => {
                    const ripple = document.createElement('div');
                    ripple.className = 'click-ripple';
                    ripple.style.left = e.clientX + 'px';
                    ripple.style.top = e.clientY + 'px';
                    ripple.style.borderColor = colors[Math.floor(Math.random() * colors.length)];
                    document.body.appendChild(ripple);
                    
                    setTimeout(() => ripple.remove(), 1000);
                }, i * 100);
            }
            
            // Tạo hạt sáng bay tứ phía
            for(let i = 0; i < 12; i++) {
                const particle = document.createElement('div');
                particle.className = 'click-particle';
                const angle = (i / 12) * Math.PI * 2;
                const distance = 80 + Math.random() * 40;
                particle.style.left = e.clientX + 'px';
                particle.style.top = e.clientY + 'px';
                particle.style.background = colors[Math.floor(Math.random() * colors.length)];
                particle.style.setProperty('--tx', Math.cos(angle) * distance + 'px');
                particle.style.setProperty('--ty', Math.sin(angle) * distance + 'px');
                document.body.appendChild(particle);
                
                setTimeout(() => particle.remove(), 1500);
            }
        });
    </script>

    <div class="container">
        <h1>🌙Quà Trung Thu🌙</h1>
        <p class="subtitle">Tụi mình là ny đúm hong zọ Xùu (❁´◡`❁)</p>
        
        <div class="divider"></div>
        
        <!-- Hình bánh Trung Thu -->
        <div class="mooncake-container">
            <div class="mooncake" id="mooncake" onclick="drawName(event)">
                <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="100" cy="100" r="80" fill="#f39c12" stroke="#d68910" stroke-width="3"/>
                    <circle cx="100" cy="100" r="80" fill="none" stroke="#8b4513" stroke-width="2" stroke-dasharray="5,5"/>
                    <circle cx="100" cy="100" r="50" fill="#e67e22" stroke="#d68910" stroke-width="2"/>
                    <text x="100" y="115" font-size="26" fill="#8b4513" text-anchor="middle" font-weight="bold">愛</text>
                    <circle cx="100" cy="40" r="5" fill="#8b4513"/>
                    <circle cx="100" cy="160" r="5" fill="#8b4513"/>
                    <circle cx="40" cy="100" r="5" fill="#8b4513"/>
                    <circle cx="160" cy="100" r="5" fill="#8b4513"/>
                    <circle cx="60" cy="60" r="4" fill="#8b4513"/>
                    <circle cx="140" cy="60" r="4" fill="#8b4513"/>
                    <circle cx="60" cy="140" r="4" fill="#8b4513"/>
                    <circle cx="140" cy="140" r="4" fill="#8b4513"/>
                </svg>
            </div>
        </div>
        
        <div class="divider"></div>
        
        <!-- Câu chúc -->
        <div class="wish-box">
            <p class="wish-text" id="wishText">{{ wish }}</p>
        </div>
        
        <!-- Countdown -->
        <div class="countdown">
            <span>Câu chúc mới sau</span>
            <div class="timer-circle" id="countdown">5</div>
            <span>giây</span>
        </div>
        
        <div class="divider"></div>
        
        <!-- Thông điệp cuối -->
        <p class="footer-message">
            Yêu em nhiều nhất trên đời! 💕
        </p>
    </div>
    
    <script>
        let countdown = 5;
        let countdownInterval;
        
        function updateCountdown() {
            countdown--;
            document.getElementById('countdown').textContent = countdown;
            
            if (countdown <= 0) {
                getNewWish();
                countdown = 5;
            }
        }
        
        function getNewWish() {
            const wishText = document.getElementById('wishText');
            wishText.classList.add('changing');
            
            setTimeout(() => {
                fetch('/api/wish')
                    .then(response => response.json())
                    .then(data => {
                        wishText.textContent = data.wish;
                        wishText.classList.remove('changing');
                    });
            }, 500);
        }
        
        // Bắt đầu countdown
        countdownInterval = setInterval(updateCountdown, 1000);
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    wish = random.choice(WISHES)
    return render_template_string(HTML_TEMPLATE, wish=wish)

@app.route('/api/wish')
def get_wish():
    return {'wish': random.choice(WISHES)}

@app.route('/fonts/<path:filename>')
def serve_font(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)





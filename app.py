from flask import Flask, render_template_string
import random

app = Flask(__name__)

# Danh sách 10 câu chúc Trung Thu ngọt ngào
WISHES = [
    "Em yêu, Trung Thu này anh chỉ muốn được ngắm trăng cùng em. Yêu em nhiều lắm! 🌕💕",
    "Bánh Trung Thu ngọt đến mấy cũng không bằng nụ cười của em. Chúc em Trung Thu vui vẻ! 🥮😊",
    "Trăng tròn là để nhớ em tròn trịa, bánh ngọt là để nhớ tình mình ngọt ngào. Yêu em! 💖🌙",
    "Trung Thu năm nay, anh muốn là chiếc bánh trong tay em, để được em giữ thật chặt! 🥮💑",
    "Em là ánh trăng sáng nhất trong đêm Trung Thu của anh. I love you to the moon and back! 🌕✨",
    "Chúc em Trung Thu an lành, hạnh phúc và luôn rạng rỡ như trăng rằm. Anh yêu em! 💕🎑",
    "Bánh Trung Thu có nhiều nhân, nhưng trái tim anh chỉ có một em thôi! 🥮❤️",
    "Trung Thu này, anh tặng em cả trái tim và cả bầu trời sao. Yêu em mãi mãi! ⭐💖",
    "Em là món quà Trung Thu đặc biệt nhất mà cuộc đời tặng cho anh. Love you! 🎁💕",
    "Ngày Trung Thu, anh chỉ cần em bên cạnh là đủ. Chúc em ngày lễ thật ngọt ngào! 🌙😘"
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trung Thu Yêu Thương 🥮💕</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            position: relative;
            overflow: hidden;
        }
        
        /* Hiệu ứng trăng phía sau */
        .moon {
            position: fixed;
            top: 10%;
            right: 15%;
            width: 200px;
            height: 200px;
            background: radial-gradient(circle at 30% 30%, #fff9e6, #ffd700);
            border-radius: 50%;
            box-shadow: 0 0 100px rgba(255, 215, 0, 0.6),
                        0 0 200px rgba(255, 215, 0, 0.4),
                        inset -30px -30px 60px rgba(0,0,0,0.1);
            animation: moonGlow 4s ease-in-out infinite;
            z-index: 1;
        }
        
        @keyframes moonGlow {
            0%, 100% { 
                box-shadow: 0 0 100px rgba(255, 215, 0, 0.6),
                           0 0 200px rgba(255, 215, 0, 0.4),
                           inset -30px -30px 60px rgba(0,0,0,0.1);
            }
            50% { 
                box-shadow: 0 0 150px rgba(255, 215, 0, 0.8),
                           0 0 250px rgba(255, 215, 0, 0.5),
                           inset -30px -30px 60px rgba(0,0,0,0.1);
            }
        }
        
        /* Hiệu ứng ngôi sao lấp lánh */
        .star {
            position: absolute;
            background: white;
            border-radius: 50%;
            animation: twinkle linear infinite;
        }
        
        @keyframes twinkle {
            0%, 100% { 
                opacity: 0;
                transform: scale(0);
            }
            50% { 
                opacity: 1;
                transform: scale(1);
            }
        }
        
        /* Hiệu ứng hoa đăng rơi */
        .lantern {
            position: absolute;
            font-size: 30px;
            animation: float-lantern linear infinite;
            opacity: 0.8;
        }
        
        @keyframes float-lantern {
            0% {
                transform: translateY(-100px) rotate(0deg);
            }
            100% {
                transform: translateY(100vh) rotate(360deg);
            }
        }
        
        /* Container chính */
        .container {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 250, 240, 0.98) 100%);
            border-radius: 40px;
            padding: 60px 50px;
            max-width: 700px;
            width: 100%;
            box-shadow: 0 40px 100px rgba(0,0,0,0.5),
                        0 0 100px rgba(255, 107, 157, 0.3),
                        inset 0 0 50px rgba(255, 255, 255, 0.3);
            text-align: center;
            position: relative;
            animation: fadeInUp 1.5s ease;
            z-index: 10;
            border: 3px solid rgba(255, 215, 0, 0.3);
        }
        
        .container::before {
            content: '';
            position: absolute;
            top: -3px;
            left: -3px;
            right: -3px;
            bottom: -3px;
            background: linear-gradient(45deg, #ff6b9d, #ffd700, #ff6b9d, #ffd700);
            border-radius: 40px;
            z-index: -1;
            animation: borderRotate 4s linear infinite;
            background-size: 400% 400%;
        }
        
        @keyframes borderRotate {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(100px) scale(0.8);
            }
            to {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }
        
        /* Hiệu ứng tim bay */
        .floating-heart {
            position: absolute;
            font-size: 20px;
            animation: floatHeart 6s ease-in-out infinite;
            opacity: 0;
        }
        
        @keyframes floatHeart {
            0% {
                transform: translateY(0) scale(0);
                opacity: 0;
            }
            10% {
                opacity: 1;
            }
            90% {
                opacity: 0.5;
            }
            100% {
                transform: translateY(-500px) scale(1.5);
                opacity: 0;
            }
        }
        
        /* Tiêu đề */
        h1 {
            background: linear-gradient(135deg, #ff6b9d, #c44569, #ff6b9d);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-size: 3em;
            margin-bottom: 15px;
            text-shadow: 0 5px 15px rgba(255, 107, 157, 0.3);
            animation: titlePulse 3s ease-in-out infinite;
            font-weight: 900;
            letter-spacing: 2px;
        }
        
        @keyframes titlePulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        .subtitle {
            color: #9b59b6;
            font-size: 1.4em;
            margin-bottom: 40px;
            font-style: italic;
            animation: subtitleFade 2s ease-in-out infinite;
        }
        
        @keyframes subtitleFade {
            0%, 100% { opacity: 0.8; }
            50% { opacity: 1; }
        }
        
        /* Hình bánh Trung Thu */
        .mooncake {
            width: 250px;
            height: 250px;
            margin: 40px auto;
            position: relative;
            animation: float 4s ease-in-out infinite;
            filter: drop-shadow(0 15px 30px rgba(243, 156, 18, 0.5));
        }
        
        @keyframes float {
            0%, 100% { 
                transform: translateY(0) rotate(0deg);
            }
            25% {
                transform: translateY(-30px) rotate(5deg);
            }
            50% { 
                transform: translateY(0) rotate(0deg);
            }
            75% {
                transform: translateY(-30px) rotate(-5deg);
            }
        }
        
        .mooncake svg {
            width: 100%;
            height: 100%;
            animation: rotateCake 20s linear infinite;
        }
        
        @keyframes rotateCake {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        
        /* Vòng tròn sáng quanh bánh */
        .mooncake::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 280px;
            height: 280px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(255,215,0,0.3), transparent);
            animation: pulse 2s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0%, 100% { 
                transform: translate(-50%, -50%) scale(1);
                opacity: 0.5;
            }
            50% { 
                transform: translate(-50%, -50%) scale(1.2);
                opacity: 0.8;
            }
        }
        
        /* Câu chúc */
        .wish-box {
            background: linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 50%, #ffeaa7 100%);
            padding: 35px;
            border-radius: 25px;
            margin: 40px 0;
            border: 4px solid #f39c12;
            position: relative;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(243, 156, 18, 0.4),
                        inset 0 0 30px rgba(255, 255, 255, 0.3);
            animation: wishBoxGlow 3s ease-in-out infinite;
        }
        
        @keyframes wishBoxGlow {
            0%, 100% {
                box-shadow: 0 10px 30px rgba(243, 156, 18, 0.4),
                           inset 0 0 30px rgba(255, 255, 255, 0.3);
            }
            50% {
                box-shadow: 0 15px 40px rgba(243, 156, 18, 0.6),
                           inset 0 0 40px rgba(255, 255, 255, 0.5);
            }
        }
        
        .wish-box::before,
        .wish-box::after {
            content: '❤️';
            position: absolute;
            font-size: 40px;
            animation: heartBeat 1.5s ease-in-out infinite;
        }
        
        .wish-box::before {
            top: 15px;
            left: 15px;
        }
        
        .wish-box::after {
            bottom: 15px;
            right: 15px;
        }
        
        @keyframes heartBeat {
            0%, 100% { 
                transform: scale(1);
                opacity: 0.3;
            }
            50% { 
                transform: scale(1.3);
                opacity: 0.6;
            }
        }
        
        .wish-text {
            font-size: 1.5em;
            color: #8b4513;
            line-height: 1.8;
            font-weight: 600;
            position: relative;
            z-index: 1;
            text-shadow: 0 2px 5px rgba(255, 255, 255, 0.5);
            transition: all 0.5s ease;
        }
        
        .wish-text.changing {
            transform: scale(0.9);
            opacity: 0.3;
        }
        
        /* Countdown timer */
        .countdown {
            margin-top: 30px;
            font-size: 1.1em;
            color: #e056fd;
            font-weight: 600;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }
        
        .timer-circle {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: linear-gradient(135deg, #667eea, #764ba2);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.3em;
            font-weight: bold;
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
            animation: timerPulse 1s ease-in-out infinite;
        }
        
        @keyframes timerPulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }
        
        /* Thông điệp cuối */
        .footer-message {
            margin-top: 40px;
            background: linear-gradient(135deg, #e056fd, #ff6b9d);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-size: 1.3em;
            font-weight: 700;
            animation: footerGlow 2s ease-in-out infinite;
            letter-spacing: 1px;
        }
        
        @keyframes footerGlow {
            0%, 100% { 
                filter: drop-shadow(0 0 5px rgba(224, 86, 253, 0.3));
            }
            50% { 
                filter: drop-shadow(0 0 15px rgba(224, 86, 253, 0.6));
            }
        }
        
        /* Responsive */
        @media (max-width: 600px) {
            .container {
                padding: 40px 25px;
            }
            h1 {
                font-size: 2.2em;
            }
            .mooncake {
                width: 180px;
                height: 180px;
            }
            .wish-text {
                font-size: 1.2em;
            }
            .moon {
                width: 120px;
                height: 120px;
                top: 5%;
                right: 5%;
            }
        }
    </style>
</head>
<body>
    <!-- Trăng phía sau -->
    <div class="moon"></div>
    
    <!-- Tạo ngôi sao lấp lánh -->
    <script>
        for(let i = 0; i < 100; i++) {
            let star = document.createElement('div');
            star.className = 'star';
            let size = Math.random() * 3 + 1;
            star.style.width = size + 'px';
            star.style.height = size + 'px';
            star.style.left = Math.random() * 100 + '%';
            star.style.top = Math.random() * 100 + '%';
            star.style.animationDuration = (Math.random() * 3 + 2) + 's';
            star.style.animationDelay = Math.random() * 5 + 's';
            document.body.appendChild(star);
        }
        
        // Tạo hoa đăng rơi
        const lanternEmojis = ['🏮', '🎋', '✨', '🌸', '🎐'];
        for(let i = 0; i < 15; i++) {
            let lantern = document.createElement('div');
            lantern.className = 'lantern';
            lantern.textContent = lanternEmojis[Math.floor(Math.random() * lanternEmojis.length)];
            lantern.style.left = Math.random() * 100 + '%';
            lantern.style.animationDuration = (Math.random() * 10 + 15) + 's';
            lantern.style.animationDelay = Math.random() * 10 + 's';
            document.body.appendChild(lantern);
        }
    </script>

    <div class="container">
        <!-- Tim bay -->
        <div class="floating-heart" style="left: 10%; animation-delay: 0s;">💕</div>
        <div class="floating-heart" style="left: 30%; animation-delay: 2s;">💖</div>
        <div class="floating-heart" style="left: 50%; animation-delay: 4s;">💗</div>
        <div class="floating-heart" style="left: 70%; animation-delay: 1s;">💝</div>
        <div class="floating-heart" style="left: 90%; animation-delay: 3s;">💞</div>
        
        <h1>🌙 Trung Thu Yêu Thương 🌙</h1>
        <p class="subtitle">Tặng gái Linh ❤️</p>
        
        <!-- Hình bánh Trung Thu SVG -->
        <div class="mooncake">
            <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                <!-- Ánh sáng bên ngoài -->
                <defs>
                    <radialGradient id="glow">
                        <stop offset="0%" style="stop-color:#ffd700;stop-opacity:0.5" />
                        <stop offset="100%" style="stop-color:#ffd700;stop-opacity:0" />
                    </radialGradient>
                </defs>
                
                <!-- Bánh ngoài -->
                <circle cx="100" cy="100" r="80" fill="url(#glow)"/>
                <circle cx="100" cy="100" r="80" fill="#f39c12" stroke="#d68910" stroke-width="4"/>
                
                <!-- Viền bánh -->
                <circle cx="100" cy="100" r="80" fill="none" stroke="#8b4513" stroke-width="3" stroke-dasharray="5,5"/>
                
                <!-- Hoa văn giữa -->
                <circle cx="100" cy="100" r="50" fill="#e67e22" stroke="#d68910" stroke-width="3"/>
                
                <!-- Chữ trên bánh -->
                <text x="100" y="115" font-size="28" fill="#8b4513" text-anchor="middle" font-weight="bold">愛</text>
                
                <!-- Hoa văn trang trí -->
                <circle cx="100" cy="40" r="6" fill="#8b4513"/>
                <circle cx="100" cy="160" r="6" fill="#8b4513"/>
                <circle cx="40" cy="100" r="6" fill="#8b4513"/>
                <circle cx="160" cy="100" r="6" fill="#8b4513"/>
                
                <!-- Hoa văn góc -->
                <circle cx="60" cy="60" r="5" fill="#8b4513"/>
                <circle cx="140" cy="60" r="5" fill="#8b4513"/>
                <circle cx="60" cy="140" r="5" fill="#8b4513"/>
                <circle cx="140" cy="140" r="5" fill="#8b4513"/>
            </svg>
        </div>
        
        <!-- Câu chúc -->
        <div class="wish-box">
            <p class="wish-text" id="wishText">{{ wish }}</p>
        </div>
        
        <!-- Countdown -->
        <div class="countdown">
            <span>Câu chúc mới sau</span>
            <div class="timer-circle" id="countdown">10</div>
            <span>giây</span>
        </div>
        
        <!-- Thông điệp cuối -->
        <p class="footer-message">
            🌟 Yêu Xùuuuuu nhìu nhất trên đời! 🌟
        </p>
    </div>
    
    <script>
        let countdown = 10;
        let countdownInterval;
        
        function updateCountdown() {
            countdown--;
            document.getElementById('countdown').textContent = countdown;
            
            if (countdown <= 0) {
                getNewWish();
                countdown = 10;
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
        
        // Tạo hiệu ứng tim bay liên tục
        setInterval(() => {
            const hearts = document.querySelectorAll('.floating-heart');
            hearts.forEach(heart => {
                heart.style.left = Math.random() * 90 + 5 + '%';
            });
        }, 6000);
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

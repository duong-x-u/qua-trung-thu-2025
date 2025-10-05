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
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            position: relative;
            overflow-x: hidden;
        }
        
        /* Hiệu ứng ngôi sao rơi */
        .star {
            position: absolute;
            width: 3px;
            height: 3px;
            background: white;
            border-radius: 50%;
            animation: fall linear infinite;
        }
        
        @keyframes fall {
            to {
                transform: translateY(100vh);
                opacity: 0;
            }
        }
        
        /* Container chính */
        .container {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 30px;
            padding: 50px 40px;
            max-width: 600px;
            width: 100%;
            box-shadow: 0 30px 60px rgba(0,0,0,0.3);
            text-align: center;
            position: relative;
            animation: fadeInUp 1s ease;
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Tiêu đề */
        h1 {
            color: #ff6b9d;
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .subtitle {
            color: #9b59b6;
            font-size: 1.2em;
            margin-bottom: 30px;
            font-style: italic;
        }
        
        /* Hình bánh Trung Thu */
        .mooncake {
            width: 200px;
            height: 200px;
            margin: 30px auto;
            position: relative;
            animation: float 3s ease-in-out infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }
        
        .mooncake svg {
            width: 100%;
            height: 100%;
            filter: drop-shadow(0 10px 20px rgba(0,0,0,0.2));
        }
        
        /* Câu chúc */
        .wish-box {
            background: linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 100%);
            padding: 25px;
            border-radius: 20px;
            margin: 30px 0;
            border: 3px solid #f39c12;
            position: relative;
            overflow: hidden;
        }
        
        .wish-box::before {
            content: '❤️';
            position: absolute;
            top: 10px;
            left: 10px;
            font-size: 30px;
            opacity: 0.3;
        }
        
        .wish-box::after {
            content: '❤️';
            position: absolute;
            bottom: 10px;
            right: 10px;
            font-size: 30px;
            opacity: 0.3;
        }
        
        .wish-text {
            font-size: 1.3em;
            color: #8b4513;
            line-height: 1.6;
            font-weight: 500;
            position: relative;
            z-index: 1;
        }
        
        /* Nút bấm */
        .btn {
            background: linear-gradient(135deg, #ff6b9d 0%, #c44569 100%);
            color: white;
            border: none;
            padding: 15px 40px;
            font-size: 1.2em;
            border-radius: 50px;
            cursor: pointer;
            margin: 10px;
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(255,107,157,0.4);
        }
        
        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(255,107,157,0.6);
        }
        
        .btn:active {
            transform: translateY(0);
        }
        
        /* Thông điệp cuối */
        .footer-message {
            margin-top: 30px;
            color: #e056fd;
            font-size: 1.1em;
            font-weight: 600;
        }
        
        /* Responsive */
        @media (max-width: 600px) {
            .container {
                padding: 30px 20px;
            }
            h1 {
                font-size: 2em;
            }
            .mooncake {
                width: 150px;
                height: 150px;
            }
            .wish-text {
                font-size: 1.1em;
            }
        }
    </style>
</head>
<body>
    <!-- Tạo ngôi sao rơi -->
    <script>
        for(let i = 0; i < 50; i++) {
            let star = document.createElement('div');
            star.className = 'star';
            star.style.left = Math.random() * 100 + '%';
            star.style.animationDuration = (Math.random() * 3 + 2) + 's';
            star.style.animationDelay = Math.random() * 5 + 's';
            document.body.appendChild(star);
        }
    </script>

    <div class="container">
        <h1>🌙 Trung Thu Yêu Thương 🌙</h1>
        <p class="subtitle">Tặng người em yêu nhất ❤️</p>
        
        <!-- Hình bánh Trung Thu SVG -->
        <div class="mooncake">
            <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                <!-- Bánh ngoài -->
                <circle cx="100" cy="100" r="80" fill="#f39c12" stroke="#d68910" stroke-width="3"/>
                <!-- Viền bánh -->
                <circle cx="100" cy="100" r="80" fill="none" stroke="#8b4513" stroke-width="2" stroke-dasharray="5,5"/>
                <!-- Hoa văn giữa -->
                <circle cx="100" cy="100" r="50" fill="#e67e22" stroke="#d68910" stroke-width="2"/>
                <!-- Chữ trên bánh -->
                <text x="100" y="110" font-size="24" fill="#8b4513" text-anchor="middle" font-weight="bold">愛</text>
                <!-- Hoa văn trang trí -->
                <circle cx="100" cy="40" r="5" fill="#8b4513"/>
                <circle cx="100" cy="160" r="5" fill="#8b4513"/>
                <circle cx="40" cy="100" r="5" fill="#8b4513"/>
                <circle cx="160" cy="100" r="5" fill="#8b4513"/>
                <!-- Hoa văn góc -->
                <circle cx="60" cy="60" r="4" fill="#8b4513"/>
                <circle cx="140" cy="60" r="4" fill="#8b4513"/>
                <circle cx="60" cy="140" r="4" fill="#8b4513"/>
                <circle cx="140" cy="140" r="4" fill="#8b4513"/>
            </svg>
        </div>
        
        <!-- Câu chúc -->
        <div class="wish-box">
            <p class="wish-text" id="wishText">{{ wish }}</p>
        </div>
        
        <!-- Nút lấy câu chúc mới -->
        <button class="btn" onclick="getNewWish()">💝 Xem Câu Chúc Khác</button>
        
        <!-- Thông điệp cuối -->
        <p class="footer-message">
            Yêu em nhiều nhất trên đời! 💕🌙✨
        </p>
    </div>
    
    <script>
        function getNewWish() {
            // Tạo hiệu ứng loading
            const wishText = document.getElementById('wishText');
            wishText.style.opacity = '0';
            
            setTimeout(() => {
                fetch('/api/wish')
                    .then(response => response.json())
                    .then(data => {
                        wishText.textContent = data.wish;
                        wishText.style.opacity = '1';
                    });
            }, 300);
        }
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

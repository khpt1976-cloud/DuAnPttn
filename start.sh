#!/bin/bash

echo "🚀 Khởi động Everon Website..."

# Khởi động backend
echo "📡 Khởi động Backend API..."
cd backend
source venv/bin/activate
python main.py &
BACKEND_PID=$!

# Đợi backend khởi động
sleep 3

# Khởi động frontend
echo "🌐 Khởi động Frontend..."
cd ../frontend
BROWSER=none npm start &
FRONTEND_PID=$!

echo "✅ Website đã khởi động!"
echo "🔗 Frontend: http://localhost:3000"
echo "🔗 Backend API: http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs"

# Hàm cleanup khi thoát
cleanup() {
    echo "🛑 Đang tắt services..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    exit 0
}

# Bắt tín hiệu Ctrl+C
trap cleanup SIGINT

# Chờ cho đến khi user nhấn Ctrl+C
wait
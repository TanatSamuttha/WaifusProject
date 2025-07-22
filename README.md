## เริ่มต้นใช้งาน

1. ดาวน์โหลดโฟล์เดอร์ Elaina
2. สร้างไฟล์ .env ในโฟล์เดอร์ Elaina
```
Elaina/.env
```
3. เนื้อหาในไฟล์ .env
```
GOOGLE_API_KEY=api key ของคุณ
```
4. รันคำสั่งนี้ใน Terminal
```
cd Elaina
uvicorn app.main:app --reload
```
5. จากนั้นเปิด Browser แล้วเข้าไปที่
```
http://localhost:8000/
```
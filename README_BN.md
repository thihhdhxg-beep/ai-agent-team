AI Agent Team — বাংলা নির্দেশিকা

প্রজেক্ট পরিচিতি

এটি AI Agent Team ও YouTube Automation System-এর প্রজেক্ট। এর মাধ্যমে AI এজেন্ট ব্যবহার করে কনটেন্ট তৈরি, ভিডিও তৈরির কাজ পরিচালনা এবং ভবিষ্যতে ভিডিও আপলোডের সুবিধা যুক্ত করা হবে।

প্রজেক্টের ফাইল

- "index.html" — ওয়েব ড্যাশবোর্ড
- "style.css" — ডিজাইন ও অ্যানিমেশন
- "app.js" — ওয়েবসাইটের ইন্টারঅ্যাকশন
- "app.py" — Python ব্যাকএন্ড
- "requirements.txt" — Python প্যাকেজের তালিকা
- ".env.example" — API সেটিংসের নমুনা
- "supabase/schema.sql" — ডেটাবেসের কাঠামো

Render সেটআপ

Build Command:
"pip install -r requirements.txt"

Start Command:
"uvicorn app:app --host 0.0.0.0 --port $PORT"

Environment Variables

Render-এর Environment Variables-এ প্রয়োজনীয় API Key ও অন্যান্য সেটিংস যোগ করতে হবে। আসল API Key কখনো GitHub-এ প্রকাশ করা যাবে না।

গুরুত্বপূর্ণ

শুধু ফাইল আপলোড করলেই সব ফিচার চালু হবে না। AI API, ব্যাকএন্ড এবং ডেটাবেসের সংযোগ সম্পূর্ণ করতে হবে। ভিডিও প্রকাশের আগে ব্যবহারকারীর অনুমোদন নেওয়ার ব্যবস্থা রাখা উচিত।

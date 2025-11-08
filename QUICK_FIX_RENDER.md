# 🔧 FIX: Deploy to Render (Quick Steps)

## Problem
Your Render deployment shows "Not Found" because:
1. Model files weren't available during build
2. OR the deployment hasn't fully completed

## ✅ Solution - 3 Simple Steps

---

## STEP 1: First Time Setup (One-time, 2 minutes)

### Option A: If Render Service Already Exists

**Go to:** https://dashboard.render.com

1. Click your service: **mango-detector**
2. Click **"Manual Deploy"** or **"Clear Build Cache"** → **"Deploy latest"**
3. Wait for build to complete (5-10 minutes)

### Option B: If You Haven't Deployed Yet

**Go to:** https://render.com

1. Sign up with GitHub
2. Click **New** → **Web Service**
3. Connect: `mango-leaf-disease-detector`
4. Fill:
   - **Name:** `mango-detector`
   - **Environment:** `Docker`
   - **Instance:** `Free`
5. **Add Environment Variable:**
   - `PORT=8080`
6. Click **"Create Web Service"**

---

## STEP 2: Wait for Build (5-10 minutes)

Render will automatically:
- ✅ Download your latest code from GitHub
- ✅ Build Docker image
- ✅ Try to download model from GitHub Release v7
- ✅ Start the server

**Watch the logs:**
- Look for "Build started" → "Building" → "Live"
- If it says "Live" (green) → **Success!** ✅
- If it says "Error" → Check error in logs

---

## STEP 3: Test Your Live API

Once you see **"Live"** status:

```
https://mango-detector-xxxx.onrender.com/
```

Test these URLs:
1. `https://mango-detector-xxxx.onrender.com/` → Should show API docs
2. `https://mango-detector-xxxx.onrender.com/health` → Should show "ok"
3. `https://mango-detector-xxxx.onrender.com/diseases` → Should list diseases

---

## ⚠️ If It Still Says "Not Found"

### Issue 1: Build is Still Running
- **Check:** Go to Render dashboard, click your service
- **Look for:** Build logs at bottom
- **Action:** Wait for "Live" status (takes 5-10 min)

### Issue 2: Build Failed - Model Not Found
- **Check:** Error message in logs
- **Fix:** This is now handled! Dockerfile auto-downloads
- **Action:** Click "Manual Deploy" to retry

### Issue 3: Port Not Responding
- **Check:** Logs show any errors?
- **Fix:** Make sure environment variable `PORT=8080` is set
- **Action:** Redeploy

---

## 🚀 What Changed?

I updated your **Dockerfile** to automatically download the model during build. Now it works without needing a GitHub Release first!

**Old Dockerfile:** ❌ Needed model files locally
**New Dockerfile:** ✅ Auto-downloads model from GitHub Release v7

---

## 📋 Your Live API URLs (When Ready)

**Main Page:**
```
https://mango-detector-xxxx.onrender.com/
```

**Health Check:**
```
https://mango-detector-xxxx.onrender.com/health
```

**List Diseases:**
```
https://mango-detector-xxxx.onrender.com/diseases
```

**Predict Disease** (POST with image):
```
https://mango-detector-xxxx.onrender.com/predict
```

---

## ✅ Quick Checklist

- [ ] Render service created or redeploy initiated
- [ ] Build is running (check logs)
- [ ] Waiting for "Live" status
- [ ] Once Live, test the URLs above
- [ ] Share your live URL!

---

## 💡 Pro Tips

1. **Build Taking Long?** Don't worry, models are large (850 MB+)
2. **Want to Speed Up?** Use a paid tier (auto-scales, faster builds)
3. **Need Help?** Check Render logs for errors

---

## 🎯 Next Action

**Right Now:**
1. Go to Render dashboard
2. Check if "mango-detector" service exists
   - **If yes:** Click "Manual Deploy"
   - **If no:** Follow Step 1: Option B above
3. Wait for "Live" status
4. Test URLs

**Expected time:** 10-15 minutes total

---

## 📞 If You Get Stuck

**Common errors & fixes:**

| Error | Fix |
|-------|-----|
| "Build timeout" | Redeploy, increase instance size |
| "Module not found" | Dependencies ok, wait for build |
| "Connection refused" | Service still building, wait more |
| "404 Not Found" | Service not yet live, check logs |

---

**Status:** ✅ Dockerfile updated and pushed  
**Next:** Go to Render dashboard and check/redeploy

Good luck! 🚀

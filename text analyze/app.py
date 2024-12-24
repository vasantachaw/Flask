from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    v, c, n, s, ss = 0, 0, 0, 0, 0
    data = {}

    if request.method == "POST":
        texts = request.form.get("text")
        
        vowels = "aeiouAEIOU"
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        numbers = "0123456789"
        symbols = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~\\"

        for char in texts:
            if char in vowels:
                v += 1
            elif char in consonants:
                c += 1
            elif char in numbers:
                n += 1
            elif char in symbols:
                s += 1
            elif char.isspace():
                ss += 1

        data = {
            "Vowels": v,
            "Consonants": c,
            "Numbers": n,
            "Symbols": s,
            "Spaces": ss,
            "Words": len(texts.split())  # Count words based on spaces
        }

        #print(f"v : {v} , c : {c} , n : {n} , s : {s} , ss : {ss}")
    
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import random

app = Flask(__name__)

def coding_decoding(st, coding):
    words = st.split(" ")
    result = []

    for word in words:
        if len(word) >= 3:
            if coding == 1:
                random_chars = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
                nword = random_chars + word[1:] + word[0] + random_chars
                result.append(nword)
            else:
                stnew = word[3:-3] if len(word) > 6 else ''  # Adjusted to handle shorter words
                nword = stnew[-1] + stnew[:-1]
                result.append(nword)
        else:
            result.append(word[::-1])

    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        st = request.form['message']
        coding = int(request.form['coding'])
        result = coding_decoding(st, coding)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
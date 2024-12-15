![alt text](cover.png)
# Paulo Sestini - Website
Code for my personal website, written using HTMX and TailwindCSS, and served with Flask on Vercel.

The website is available on [paulosestini.xyz](https://paulosestini.xyz)

## Requirements
Python and Node

## Setup

Install Node dependencies (TailwindCSS)

```
npm install
```

Install Python dependencies (Flask)

```
pip install -r requirements.txt
```

## Running local dev server

Start tailwind on watch mode

```
npx tailwindcss -i ./src/input.css -o ./src/output.css --watch
```

Start Flask server

```
python app.py
```

Open browser and navigate to `http://localhost:5000`

## Deploying

Before deploying, the CSS must be compiled:

```
npx tailwindcss -i ./src/input.css -o ./src/output.css
```

Then, after the changes are pushed to the repository, the website is automatically deployed to Vercel.

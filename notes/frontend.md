# Node.js

|cmd|note|
|:-|:-|
|`node -v` `npm -v`|run local javascript|
|`npm init -y`|+ `package.json`|
|`npm install`|`node_modules` + : code `[module]/` + exe `.bin/[module]` <br> `package.json`: `devDependencies` (tool) <br> `.gitignore`: `node_modules` (reinstall from `package.json`)|
|`npm run`|`node_modules/.bin` <br> `package.json`: |

# Vite

#BuildTool

#### 1. Configuration

- **modern frontend:** balance demands between **engineering: standard**, **user: faster & comfort** and **developer: efficiency & performance**
- **install:** `npm install -D vite`
- **run:** `node_modules/.bin/vite` + ` /build/preview`
- **config** 
```json
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }
```

|cmd|note|
|:-|:-|
|`npm run dev`|src code + local server + **hot update**|
|`npm run build`|`dist` code (launch version) + **compress requests** <br> + **hash cache** <br> `.gitignore`: `dist`|
|`npm run preview`|local server + preview `dist`|

# React

#Framework

#### 1. Configuration
- **install:** `npm install react react-dom` 
- **config:** `npm install -D @vitejs/plugin-react` (vite translater)
```javascript
// /vite.config.js
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
    plugins: [react()],
});
```
`package.json`: + `"type": "module"`
- **init:** `npm create vite`

#### 2. Structure

- **platform:** `index.html`
- **entrance:** `main.jsx` (hub of components)
- **components:** `App.jsx` (integrate & control page components) + `[page].jsx` (page components) + `[card].jsx` (cardinal components)
- **props&state:** `data` + `router`

```text
index.html
|- src
    |- main.jsx
    |- App.jsx
    |- components/
        |- [page].jsx
        |- [card].jsx
    |- css/
    |- data/
    |- router/
```
- **.jsx:** 1. React `js` func return `html` structure import `css` style; 2. resuable UI component / module

# Vanilla

#### 1. ES: module (CDN / npm)

**server link**

* `[module].js` - `import & export` 
* `main.js` - `import` - `[module].js`

#### 2. Structure

- **html**
- **css**
- **javascript**

```text
index.html
|- css\
|- js\
```

# HTML

```html
<!DOCTYPE html>
<html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>frontend</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <div class="card">
            <h1>Hello, Internet<h1>
            <p>Server: URL, Ubuntu 24.04 LTS, Nginx, SSH + Git</p>
            <p>DNS: website - IP (public network) - server - port - nginx - doc</p>
            <p>Port: http 80 / https 443(encrypt) / SSH: 22</p>
            <p id="msg"> This is a HTML + CSS page.</p>
            <button onclick="changeText()">Click here.</button>
        </div>
    </body>
```

# CSS

```css
body {
    background-color: #f0f4f8;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
    font-family: sans-serif;
}

.card {
    background: white;
    padding: 40px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

h1 {
    color: #2c3e50;
    margin-bottom: 12px;
}

p {
    color: #666;
}

button {
    margin-top: 20px;
    padding: 10px 24px;
    background-color: #3498db;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 16px;
}

button:hover {
    background-color: #2980b9;
}
```

# JavaScript

```javascript
function changeText() {
    document.getElementById('msg').textContent = 'This is a JavaScript page.';
}
```

# JSON

```json
{
  "name": "tech-stack",
  "version": "1.0.0"
}
```

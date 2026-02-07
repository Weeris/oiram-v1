# Oiram-V1

A simple Oiram-style platformer game built with Streamlit and HTML5 Canvas.

## 🎮 Game Features (MVP)

### Player Controls
- **Arrow Left/Right**: Move left/right
- **Space / Arrow Up**: Jump
- **R**: Restart game

### Game Elements
- **Oiram**: The player character (red square with hat)
- **Ground**: Platforms to stand on
- **Goomba**: Enemy that moves back and forth
- **Coins**: Collectible items (+10 points)
- **Flagpole**: Reach the end to win

### Game Rules
- Collect coins for score
- Avoid Goomba (touching = game over)
- Reach the flagpole to win
- Score is displayed at top

---

## 🚀 How to Play

### Local Development
```bash
cd oiram-v1
pip install streamlit
streamlit run app.py
```

### Online
Access the game via Streamlit Cloud deployment.

---

## 📁 Project Structure

```
oiram-v1/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── app.py                 # Main Streamlit application
├── games/
│   └── oiram.html         # HTML5 Canvas game engine
├── .streamlit/
│   └── config.toml        # Streamlit configuration
└── .gitignore
```

---

## 🛠️ Development Phases

### Phase 1: Foundation (Complete)
- [x] Project structure
- [x] Basic HTML5 Canvas game
- [x] Player movement (left/right/jump)
- [x] Gravity and collision detection
- [x] Ground platforms

### Phase 2: Game Elements (Complete)
- [x] Goomba enemy
- [x] Coins collectibles
- [x] Flagpole win condition
- [x] Score display

### Phase 3: Polish (Next)
- [ ] Sound effects
- [ ] Multiple levels
- [ ] High score system
- [ ] Power-ups

---

## 🎯 Technical Details

### Game Engine
- **HTML5 Canvas** for rendering
- **JavaScript** for game logic
- **RequestAnimationFrame** for smooth animation (60fps)

### Streamlit Integration
- **st.components.html** to embed game
- Custom CSS for game container styling

---

## 📝 Notes for Development

### Running Locally
```bash
# Start the game
streamlit run app.py

# The game will open at http://localhost:8501
```

### Game Controls
- Use arrow keys to move
- Space or up arrow to jump
- R to restart

### Level Design
- The level is 3000 pixels wide
- Camera follows the player
- Multiple platforms and enemies

---

## 📝 License

MIT License - Feel free to modify and share!

---

## 👨‍💻 Author

Built with ❤️ using Streamlit and HTML5 Canvas


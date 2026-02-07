"""
Oiram-V1: A Oiram-style platformer game built with Streamlit and HTML5 Canvas.
"""

import streamlit as st
import os

# Page configuration
st.set_page_config(
    page_title="Oiram-V1",
    page_icon="🍄",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for the game
st.markdown("""
<style>
    .game-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0 auto;
        border: 4px solid #1e3a5f;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    
    .game-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        color: #e3001b;
        text-shadow: 3px 3px 0 #000;
        margin-bottom: 1rem;
    }
    
    .game-subtitle {
        text-align: center;
        font-size: 1rem;
        color: #666;
        margin-bottom: 2rem;
    }
    
    .controls-info {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        margin-top: 1rem;
        font-family: monospace;
    }
    
    .stApp {
        background: linear-gradient(180deg, #5c94fc 0%, #87ceeb 100%);
        min-height: 100vh;
    }
</style>
""", unsafe_allow_html=True)

def load_game_html():
    """Load the game HTML from the games directory."""
    game_path = os.path.join(os.path.dirname(__file__), "games", "oiram.html")
    try:
        with open(game_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        st.error("Game file not found! Please ensure games/oiram.html exists.")
        return None

def main():
    """Main Streamlit app function."""
    # Title
    st.markdown('<div class="game-title">🍄 Super Oiram-V1 🍄</div>', unsafe_allow_html=True)
    st.markdown('<div class="game-subtitle">A simple platformer game built with Streamlit</div>', unsafe_allow_html=True)
    
    # Load and display the game
    game_html = load_game_html()
    if game_html:
        # Embed the game with custom styling
        st.markdown('<div class="game-container">', unsafe_allow_html=True)
        game_html_with_height = game_html.replace(
            'height: 400px;',
            'height: 480px;'
        )
        st.components.v1.html(
            game_html_with_height,
            height=500,
            scrolling=False
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Controls info
        st.markdown("""
        <div class="controls-info">
            <strong>🎮 Controls:</strong><br>
            ← → : Move Left/Right<br>
            Space / ↑ : Jump<br>
            R : Restart Game
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #888; font-size: 0.8rem;'>"
        "Built with ❤️ using Streamlit and HTML5 Canvas | "
        "<a href='https://github.com/Weeris/oiram-v1' target='_blank'>GitHub</a>"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

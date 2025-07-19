import streamlit as st
from datetime import datetime, time
import random
import uuid
import time as pytime
import time as pytime
from datetime import datetime, time, timedelta
import base64

# --- Page Config ---
st.set_page_config(
    page_title="Wie Annica lernen kann",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS-Block ---
st.markdown ("""
<style>
    /* Root Variables */
    :root {
        /* Hauptfarbpalette - 5 harmonische rote Pastelltöne basierend auf #880608 */
        --color-1: #F4E6E7;  /* Sehr helles Rosé */
        --color-2: #E8C1C5;  /* Sanftes Rosa */
        --color-3: #D89DA3;  /* Mittleres Rosa */
        --color-4: #C87882;  /* Kräftigeres Rosa */
        --color-5: #B85461;  /* Intensives Rosa (basierend auf #880608) */
        
        /* Gradients */
        --primary-gradient: linear-gradient(135deg, var(--color-1) 0%, var(--color-2) 100%);
        --secondary-gradient: linear-gradient(135deg, var(--color-2), var(--color-3));
        --card-bg: rgba(255, 255, 255, 0.95);
        --text-primary: #000000;
        --text-secondary: #333333;
        --accent-pink: var(--color-4);
        --accent-light: var(--color-5);
    }
    
    /* Global Styles */
    .stApp {
        background: var(--primary-gradient);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        min-height: 100vh;
    }

    /* Zentriertes Layout */
    .main .block-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 1rem 2rem;
    }    

    /* Streamlit Standard-Container überschreiben */
    .st-emotion-cache-1y4p8pa {
        max-width: 1200px;
        padding: 2rem 1rem;
    }

    section[data-testid="stSidebar"] {
        display: none;
    }

    /* Hauptinhalt zentrieren */
    .main {
        display: flex;
        justify-content: center;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Container-Anpassungen */
    .main .block-container {
        max-width: 1200px;
        padding: 1rem;
        margin: 0 auto;
    }

    /* Tabs größer und präsenter */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(255, 255, 255, 0.3) !important;
        padding: 0.5rem !important;
        border-radius: 15px !important;
        margin-bottom: 1.5rem !important;
    }

    .stTabs [data-baseweb="tab"] {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        padding: 0.8rem 1.5rem !important;
        min-height: 50px !important;
        background: var(--color-5) !important;
        color: black !important;
        border-radius: 12px !important;
        margin: 0 0.2rem !important;
    }

    .stTabs [aria-selected="true"] {
        background: white !important;
        color: black !important;
        box-shadow: 0 4px 12px rgba(200, 159, 163, 0.3) !important;
    }

    /* Metriken kleiner */
    .metric-card {
        padding: 0.5rem !important;
        margin-bottom: 0.5rem !important;
    }

    .metric-value {
        font-size: 1.2rem !important;
    }

    .metric-label {
        font-size: 0.7rem !important;
    }
    
    /* Karten-Design */
    .custom-card {
        background: white !important;
        border-radius: 15px;
        padding: 1.5rem;
        color: black !important;
        margin-bottom: 1rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Metric Cards */
    .metric-card {
        background: rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        backdrop-filter: blur(10px);
        color: white !important;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        margin: 0;
    }
    
    .metric-label {
        font-size: 0.8rem;
        opacity: 0.9;
        margin-top: 0.5rem;
    }
    
    /* Mobile Anpassungen */
    @media (max-width: 768px) {
        .stTabs [data-baseweb="tab"] {
            font-size: 0.9rem !important;
            padding: 0.6rem 0.8rem !important;
            min-height: 40px !important;
        }
        .main .block-container {
            max-width: 100%;
            padding: 0.5rem;
            margin: 0 auto;
        }
        
        .custom-card {
            padding: 1rem;
            background: white !important;
            color: black !important;
        }
        
        .metric-value {
            font-size: 1.5rem;
        }
        
        /* Tabs mobil-freundlicher */
        .stTabs [data-baseweb="tab-list"] {
            gap: 0.25rem;
        }
        
        .stTabs [data-baseweb="tab"] {
            padding: 0.5rem;
            font-size: 0.8rem;
        }
    }
    
    /* Buttons */
    .stButton > button {
        background: var(--color-5) !important;
        color: black !important;
        border: 1px solid var(--color-4) !important;
        border-radius: 25px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(200, 159, 163, 0.2);
    }

    .stButton > button:hover {
        background: var(--color-2) !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(200, 159, 163, 0.3);
    }
    
    /* Success/Warning/Info Messages */
    .stSuccess, .stWarning, .stInfo {
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
    }

    .anleitung-box {
        background: white !important;
        color: black !important;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid var(--color-4);
    }

    .anleitung-button {
        background: white !important;
        color: black !important;
        border: 2px solid var(--color-4) !important;
    }

    /* Pinnwand Styles (behält bunte Post-Its) */
    .pinnwand {
        background: var(--color-2) !important;
        border: 10px solid var(--color-4) !important;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
        min-height: 400px;
        position: relative;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# --- Session State Initialisierung ---
if "initialized" not in st.session_state:
    st.session_state.initialized = True

    st.session_state.pause_statistics = {
        "solo_pausen": 0,
        "gruppen_pausen": 0,
        "total_time": 0,
        "trave_spaziergaenge": 0,
        "wakenitz_besuche": 0,
        "mensa_pausen": 0,
        "meditation_minuten": 0,
        "bewegung_minuten": 0
    }
    
    st.session_state.countdown_active = False
    st.session_state.countdown_time = 120
    st.session_state.current_solo_activity = None
    st.session_state.conversation_history = []
    st.session_state.favorite_questions = []
    st.session_state.conversation_badges = {
        "icebreaker": False,
        "deep_diver": False,
        "empathy_master": False,
        "story_collector": False,
        "connection_builder": False
    }
    st.session_state.learning_timer_active = False
    st.session_state.timer_start = None
    st.session_state.current_interval = None
    st.session_state.interval_count = 0
    st.session_state.total_learning_time = 0
    st.session_state.selected_method = None
    st.session_state.woop_goals = {
        "wish": "",
        "outcome": "",
        "obstacle": "",
        "plan": ""
    }



# --- Helper Funktion für kleine Metriken ---
def show_mini_metrics():
    """Zeigt kleine Metriken am unteren Rand"""
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card" style="background: rgba(255,255,255,0.05);">
            <p class="metric-value">{len(st.session_state.groups)}</p>
            <p class="metric-label">Gruppen</p>
        </div>
        """, unsafe_allow_html=True)
    
    
    with col3:
        total_pauses = st.session_state.pause_statistics["solo_pausen"] 
        st.markdown(f"""
        <div class="metric-card" style="background: rgba(255,255,255,0.05);">
            <p class="metric-value">{total_pauses}</p>
            <p class="metric-label">Pausen</p>
        </div>
        """, unsafe_allow_html=True)
    
    </div>
    """, unsafe_allow_html=True)

# --- Haupttitel mit Level ---
st.markdown('<h1 style="text-align: center; color: #8b0000; font-size: 5rem; margin-bottom: -1rem;">Wie Annica lernen kann</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #8b0000; font-size: 1.8rem; margin-top: 0; margin-bottom: 1rem;">Ich glaube an dich</p>', unsafe_allow_html=True)

    
# Tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "momentaner Stand der Dinge", 
    "Escapism", 
    "Lerntipps",
    "Pausenraum",
    "Wie ich gerne lerne",
    "Klausurenplaner", 
    "Intervalllernen"
])


with tab1:
    st.markdown(
        '<h1 style="color: #8b3a3a;">momentaner Stand der Dinge</h1>',
        unsafe_allow_html=True
    )
    
    </div>
    """, unsafe_allow_html=True)
          
            st.markdown("---")
               

with tab2:
    st.header("Escpaism")
    

with tab3:
    st.header("Lerntipps")
    
            st.markdown("---")
           
       
with tab4: 
    st.markdown(
        '<h1 style="color: #8b3a3a;">Gesunde Pausen für Körper & Geist</h1>',
        unsafe_allow_html=True
    )
   
    
    st.markdown("""
    <div class="custom-card" style="background: #ffe4e1; border-left: 4px solid #8b3a3a;">
        <p style="margin: 0; color: #8b3a3a;">
            <strong>Du bist nicht allein!</strong> Es ist völlig okay und sogar richtig wichtig beim 
            Lernen Pausen zu machen. Dein Gehirn braucht diese kleinen Auszeiten, 
            um das Gelernte zu verarbeiten und neue Energie zu tanken. Statt dich durchzubeißen, 
            helfen dir bewusste Pausen dabei, konzentrierter und entspannter weiterzumachen. 
            Gönn dir also ruhig mal eine Pause!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Pausentyp wählen
    pause_type = st.radio(
        "Wie möchtest du deine Pause verbringen?",
        ["🧘 Solo-Pause (Zeit für mich)", "👥 Gruppen-Pause (Gemeinsam entspannen)"],
        horizontal=True
    )
    
    st.markdown("---")
    
    
    # Aktivitäten
    if "Solo-Pause" in pause_type:
        st.subheader("🌊 Solo-Aktivitäten")
        
        # Aktivitätskategorie wählen
        activity_cat = st.selectbox(
            "Was brauchst du gerade?",
            ["🏠 Vor Ort (Zimmer/Bibliothek)", "🚶 Bewegung (Rausgehen)", "🌿 Natur (Lübeck erkunden)"]
        )
        
        # Aktivitäten nach Kategorie
        activities = {
            "🏠 Vor Ort (Zimmer/Bibliothek)": [
                {
                    "name": "Schreibtisch-Yoga",
                    "duration": "3 Min",
                    "location": "Dein Arbeitsplatz",
                    "description": "Dehne Nacken, Schultern und Rücken direkt am Schreibtisch",
                    "anleitung": "1. Schultern kreisen (10x vor, 10x zurück)\n2. Kopf langsam von Seite zu Seite\n3. Arme über Kopf strecken\n4. Rücken durchstrecken",
                    "stamps": 1
                },
                {
                    "name": "Fenster-Meditation",
                    "duration": "5 Min",
                    "location": "Am Fenster",
                    "description": "Schaue aus dem Fenster und beobachte ohne zu bewerten",
                    "anleitung": "1. Fenster öffnen für frische Luft/n2. 5 Dinge die du siehst/n3. 4 Geräusche die du wahrnimmst/n4. 3 tiefe Atemzüge/n5. Gedanken ziehen lassen als wären sie Wolken",
                    "stamps": 1
                },
                {
                    "name": "Tee-Zeremonie",
                    "duration": "10 Min",
                    "location": "Küche/Pausenraum",
                    "description": "Bewusst Tee kochen und trinken - volle Achtsamkeit",
                    "anleitung": "1. Wasser bewusst aufkochen\n2. Tee mit Bedacht auswählen\n3. Während des Ziehens nur warten\n4. Ersten Schluck 30 Sek im Mund\n5. Wärme spüren",
                    "stamps": 1
                },
                {
                    "name": "Power-Nap",
                    "duration": "10 Min",
                    "location": "Ruhige Ecke",
                    "description": "Kurzer Powernap für neue Energie (Timer stellen!)",
                    "anleitung": "1. Timer auf 10 Min stellen\n2. Augen schließen\n3. An nichts denken\n4. Wenn Gedanken kommen:'lass sie rein und wieder weiterziehen, wie die Wolken, werte sie nicht'\n5. Nach Timer: Strecken!",
                    "stamps": 1
                }
            ],
            "🚶 Bewegung (Rausgehen)": [
                {
                    "name": "Treppen-Workout",
                    "duration": "5 Min",
                    "location": "Treppenhaus",
                    "description": "Rauf und runter - Kreislauf aktivieren",
                    "anleitung": "1. 2x normal hoch und runter\n2. 1x zwei Stufen auf einmal\n3. 1x seitlich gehen\n4. Oben 10 Hampelmänner\n5. Unten dehnen",
                    "stamps": 1
                },
                {
                    "name": "Campus-Runde",
                    "duration": "10 Min",
                    "location": "Um den Campus",
                    "description": "Einmal ums Gebäude - frische Luft tanken",
                    "anleitung": "1. Zügig gehen (nicht schlendern)\n2. Bewusst atmen: 4 ein, 4 aus\n3. Himmel beobachten\n4. 3 schöne Details entdecken\n5. Lächeln!",
                    "stamps": 1
                },
                {
                    "name": "Mensa-Terrassen-Pause",
                    "duration": "10 Min",
                    "location": "Mensa Dachterrasse",
                    "description": "Frische Luft mit Aussicht über Lübeck",
                    "anleitung": "1. Zur Terrasse gehen\n2. Aussicht genießen\n3. 5 tiefe Atemzüge\n4. Arme weit ausbreiten\n5. Energie tanken",
                    "stamps": 1
                }
            ],
            "🌿 Natur (Lübeck erkunden)": [
                {
                    "name": "Wakenitz-Meditation",
                    "duration": "20 Min",
                    "location": "Wakenitz-Ufer (5 Min vom Campus)",
                    "description": "Entspannung am 'Amazonas des Nordens'",
                    "anleitung": "1. Zum Wakenitz-Ufer radeln/gehen\n2. Ruhigen Platz suchen\n3. Wasser beobachten\n4. Enten zählen\n5. Gedanken mit dem Wasser fließen lassen",     
                    "stamps": 2
                },
                {
                    "name": "Trave-Spaziergang",
                    "duration": "15 Min",
                    "location": "Trave-Promenade",
                    "description": "Bewegung mit Blick auf die Altstadt",
                    "anleitung": "1. Zur Trave gehen\n2. Richtung Holstentor\n3. Schiffe beobachten\n4. 3 Fotos machen\n5. Auf Bank 2 Min sitzen",  
                    "stamps": 2
                },
                {
                    "name": "Holstentor-Auszeit",
                    "duration": "15 Min",
                    "location": "Holstentor",
                    "description": "Geschichte trifft Gegenwart - Perspektivwechsel",
                    "anleitung": "1. Zum Holstentor (Rad/Bus)\n2. Details am Tor entdecken\n3. Touristen beobachten\n4. Selfie mit Tor\n5. Niederegger-Marzipan als Belohnung?",           
                    "stamps": 2
                },
                {
                    "name": "Dom-Besuch",
                    "duration": "15 Min",
                    "location": "Lübecker Dom",
                    "description": "Ruhe in historischen Mauern finden",
                    "anleitung": "1. Zum Dom gehen\n2. Einmal durchgehen\n3. Kerze anzünden (optional)\n4. 5 Min still sitzen\n5. Akustik genießen",              
                    "stamps": 2
                }
            ]
        }
        
        # Zufällige Aktivität aus gewählter Kategorie
        if st.button("Zufällige Aktivität", key="random_activity"):
            available_activities = activities.get(activity_cat, [])
            if available_activities:
                st.session_state.current_solo_activity = random.choice(available_activities)
        
        # Aktivität anzeigen
        if st.session_state.current_solo_activity:
            activity = st.session_state.current_solo_activity
            
            st.markdown(f"""
            <div class="custom-card" style="border-left: 4px solid #059669;">
                <h4>📍 {activity['name']}</h4>
                <p><strong>Ort:</strong> {activity['location']} | <strong>Dauer:</strong> {activity['duration']}</p>
                <p style="font-style: italic;">{activity['description']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander("Anleitung"):
                st.markdown(f'<div class="anleitung-box">{activity.get("anleitung", "Keine Anleitung verfügbar")}</div>', unsafe_allow_html=True)
                st.markdown('<style>div.row-widget.stButton:nth-of-type(1) > button {background: #F5E6D3 !important; color: black !important;}</style>', unsafe_allow_html=True)
           
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Pause gemacht!", key="done_activity", type="primary"):
                    st.session_state.pause_statistics["solo_pausen"] += 1
                    st.session_state.reward_stamps += activity['stamps']
                    
                    # Spezifische Statistiken
                    if "Wakenitz" in activity['name']:
                        st.session_state.pause_statistics["wakenitz_besuche"] += 1
                    if "Trave" in activity['name']:
                        st.session_state.pause_statistics["trave_spaziergaenge"] += 1
                    if "Bewegung" in activity_cat:
                        st.session_state.pause_statistics["bewegung_minuten"] += int(activity['duration'].split()[0])
                   
                    old_level = st.session_state.user_level
                    new_level, new_avatar, _ = calculate_user_level()
                    if new_level != old_level:
                        st.balloons()
                        st.success(f"Level Up! Du bist jetzt: {new_avatar} {new_level}!")
                    st.success(f"Super! +{activity['stamps']} Stempel für deine Pause!")
                    st.session_state.current_solo_activity = None
                    st.rerun()
            
            with col2:
                if st.button("Andere Aktivität", key="other_activity"):
                    st.session_state.current_solo_activity = None
                    st.session_state.current_solo_activity = None
                    st.rerun()


    # 2-Minuten Countdown (einfache Version)
    st.subheader("Die 2-Minuten-Nichtstun-Challenge")

    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.write("Nimm dir 2 Minuten nur für dich. Kein Handy, keine Ablenkung. Nur du und eine Gedanken (spooky)")
    with col2:
        # Externe Timer-Links
        st.link_button("Online Timer", "https://donothingfor2minutes.org")
    with col3:
        if st.button("Fertig", key="timer_done"):
            st.session_state.pause_statistics["meditation_minuten"] += 2
            st.session_state.pause_statistics["solo_pausen"] += 1
            st.session_state.reward_stamps += 1
            st.success("Super! 2 Minuten Ruhe - das hast du dir verdient! +1 Stempel")
            st.balloons()

    st.info("Starte den Timer, lege dein Handy weg und konzentriere dich nur auf deine Atmung und Umgebung.")

    st.markdown("---")
    
   
with tab5:
    st.header("Gemeinschaftsraum")
    
   
with tab6:
    st.header("Gesprächsfetzen")
    
   
with tab7: 
    st.markdown("---")
    st.header("⏰ Wissenschaftliche Lernintervalle & Timer")

    st.markdown("""
    <div class="custom-card" style="background: linear-gradient(135deg, #E0F2FE, #DBEAFE); border-left: 4px solid #2563EB;">
        <p style="margin: 0; color: #1E40AF;">
            <strong>Optimiere deine Lernzeit!</strong> 
            Nutze wissenschaftlich fundierte Intervalle für maximale Produktivität und Erholung.
            Die App erinnert dich automatisch an Pausen.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Lernmethoden Definition
    learning_methods = {
        "🧠 Auswendiglernen": {
            "description": "Viele kurze Pausen zum Abspeichern",
            "work_time": 20,
            "break_time": 5,
            "long_break": 15,
            "cycles_before_long": 4,
            "color": "#F59E0B",
            "tips": [
                "Nutze die Pausen zum mentalen Wiederholen",
                "Schließe die Augen und rufe das Gelernte ab",
                "Mache in der Pause leichte Bewegungen"
            ]
        },
        "📚 Neue Inhalte erarbeiten": {
            "description": "Längere Intervalle zum Vertiefen",
            "work_time": 45,
            "break_time": 10,
            "long_break": 30,
            "cycles_before_long": 3,
            "color": "#10B981",
            "tips": [
                "Nutze die Pausen zum Reflektieren",
                "Schreibe Kerngedanken auf",
                "Lasse deinen Geist wandern"
            ]
        },
        "🎯 60-60-30 Methode": {
            "description": "Hochfokussierte Arbeit mit längerer Erholung",
            "work_time": 55,
            "break_time": 5,
            "long_break": 30,
            "cycles_before_long": 2,
            "color": "#8B5CF6",
            "special_cycle": [55, 5, 60, 30],  # Spezieller Zyklus
            "tips": [
                "Erste 55 Min: Volle Konzentration",
                "5 Min Pause: Kurz durchatmen",
                "Nächste 60 Min: Deep Work",
                "30 Min Pause: Richtig erholen"
            ]
        },
        "🍅 Pomodoro Classic": {
            "description": "Der Klassiker für Fokus",
            "work_time": 25,
            "break_time": 5,
            "long_break": 20,
            "cycles_before_long": 4,
            "color": "#EF4444",
            "tips": [
                "Eine Aufgabe pro Pomodoro",
                "Keine Unterbrechungen erlaubt",
                "Pausen sind heilig"
            ]
        },
        "🌊 Flow-State (90-20)": {
            "description": "Ultradiane Rhythmen nutzen",
            "work_time": 90,
            "break_time": 20,
            "long_break": 30,
            "cycles_before_long": 2,
            "color": "#06B6D4",
            "tips": [
                "Folge deinem natürlichen Rhythmus",
                "90 Min = optimale Konzentrationsspanne",
                "20 Min Pause für echte Erholung"
            ]
        }
    }

    # WOOP-Methode Integration
    with st.expander("🎯 WOOP-Methode: Plane deine Lernziele"):
        st.markdown("""
        **WOOP** (Wish, Outcome, Obstacle, Plan) hilft dir, realistische Ziele zu setzen und zu erreichen.
        """)
    
        col1, col2 = st.columns(2)
        with col1:
            st.session_state.woop_goals["wish"] = st.text_area(
                "🌟 **W**ish - Was möchtest du heute schaffen?",
                value=st.session_state.woop_goals["wish"],
                placeholder="z.B. Kapitel 5 verstehen und zusammenfassen"
            )
            st.session_state.woop_goals["outcome"] = st.text_area(
                "✨ **O**utcome - Wie wirst du dich fühlen?",
                value=st.session_state.woop_goals["outcome"],
                placeholder="z.B. Erleichtert und stolz auf mich"
            )
    
        with col2:
            st.session_state.woop_goals["obstacle"] = st.text_area(
                "🚧 **O**bstacle - Was könnte dich hindern?",
                value=st.session_state.woop_goals["obstacle"],
                placeholder="z.B. Instagram-Ablenkung, Müdigkeit"
            )
            st.session_state.woop_goals["plan"] = st.text_area(
                "📋 **P**lan - Wenn-Dann-Plan",
                value=st.session_state.woop_goals["plan"],
                placeholder="z.B. Wenn ich müde werde, dann mache ich 5 Min Bewegung"
            )

    # Methodenauswahl
    col1, col2 = st.columns([2, 1])
    
    with col1:
        selected_method = st.selectbox(
            "Wähle deine Lernmethode:",
            options=list(learning_methods.keys()),
            help="Jede Methode ist für unterschiedliche Lernziele optimiert"
        )

    with col2:
        method = learning_methods[selected_method]
        st.markdown(f"""
        <div style="background: {method['color']}; color: white; padding: 1rem; 
                    border-radius: 10px; text-align: center;">
            <strong>{method['description']}</strong>
        </div>
        """, unsafe_allow_html=True)

    # Timer-Kontrollen
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if not st.session_state.learning_timer_active:
            if st.button("▶️ Timer starten", type="primary", use_container_width=True):
                st.session_state.learning_timer_active = True
                st.session_state.timer_start = datetime.now()
                st.session_state.selected_method = selected_method
                st.session_state.current_interval = "work"
                st.session_state.interval_count = 0
            
                # Browser-Notifikation aktivieren
                st.markdown("""
                <script>
                if ("Notification" in window) {
                    Notification.requestPermission();
                }
                </script>
                """, unsafe_allow_html=True)
            
                st.success("Timer gestartet! Viel Erfolg beim Lernen! 📚")
                st.rerun()
        else:
            if st.button("⏸️ Pausieren", use_container_width=True):
                st.session_state.learning_timer_active = False
                st.info("Timer pausiert")
                st.rerun()

    with col2:
        if st.button("⏹️ Stoppen", use_container_width=True):
            if st.session_state.timer_start:
                duration = (datetime.now() - st.session_state.timer_start).seconds // 60
                st.session_state.total_learning_time += duration
            st.session_state.learning_timer_active = False
            st.session_state.timer_start = None
            st.session_state.current_interval = None
            st.success(f"Gut gemacht! Du hast {duration} Minuten gelernt!")
            st.rerun()
    
    with col3:
        if st.button("🔄 Reset", use_container_width=True):
            st.session_state.interval_count = 0
            st.session_state.current_interval = None
            st.info("Timer zurückgesetzt")
            st.rerun()

    with col4:
        st.metric("Intervalle", st.session_state.interval_count)

    # Timer-Anzeige
    if st.session_state.learning_timer_active and st.session_state.timer_start:
        method = learning_methods[st.session_state.selected_method]
    
        # Berechne verbleibende Zeit
        elapsed = (datetime.now() - st.session_state.timer_start).seconds
    
        if st.session_state.current_interval == "work":
            total_time = method['work_time'] * 60
            interval_type = "🎯 Lernzeit"
            next_interval = "Pause"
        else:
            total_time = method['break_time'] * 60
            interval_type = "☕ Pause"
            next_interval = "Lernzeit"
    
        remaining = max(0, total_time - elapsed)
        progress = min(1.0, elapsed / total_time)
    
        # Timer-Display
        st.markdown(f"""
        <div class="custom-card" style="background: linear-gradient(135deg, #FEF3C7, #FDE68A); 
                                        text-align: center; padding: 2rem;">
            <h2 style="color: #92400E; margin: 0;">{interval_type}</h2>
            <h1 style="color: #78350F; font-size: 4rem; margin: 1rem 0;">
                {remaining // 60:02d}:{remaining % 60:02d}
            </h1>
            <p style="color: #92400E;">Nächste Phase: {next_interval}</p>
        </div>
        """, unsafe_allow_html=True)
    
        # Progress Bar
        st.progress(progress)
    
        # Automatischer Übergang
        if remaining == 0:
            if st.session_state.current_interval == "work":
                st.session_state.current_interval = "break"
                st.session_state.interval_count += 1
            
                # Notifikation
                st.markdown("""
                <script>
                if ("Notification" in window && Notification.permission === "granted") {
                    new Notification("Zeit für eine Pause! 🎉", {
                        body: "Du hast es geschafft! Zeit zum Entspannen.",
                        icon: "🎯"
                    });
                    }
                </script>
                """, unsafe_allow_html=True)
            
                st.balloons()
                st.success("🎉 Geschafft! Zeit für eine Pause!")
            else:
                st.session_state.current_interval = "work"
            
                st.markdown("""
                <script>
                if ("Notification" in window && Notification.permission === "granted") {
                    new Notification("Zurück ans Werk! 💪", {
                        body: "Die Pause ist vorbei. Auf geht's!",
                        icon: "📚"
                    });
                }
                </script>
                """, unsafe_allow_html=True)
            
                st.info("Pause vorbei! Weiter geht's! 💪")
        
            st.session_state.timer_start = datetime.now()
            pytime.sleep(2)
            st.rerun()

    # Pausenaktivitäten für Lernintervalle
    if st.session_state.current_interval == "break":
        st.markdown("---")
        st.subheader("🌟 Optimale Pausenaktivitäten")
    
        pause_activities = {
            "🕺 Bewegung & Tanz": [
                {"name": "Aerobic-Tanz", "time": "3-5 Min", "benefit": "Aktiviert Kreislauf & Gehirn"},
                {"name": "Yoga-Flow", "time": "5 Min", "benefit": "Löst Verspannungen"},
                {"name": "Hampelmänner", "time": "2 Min", "benefit": "Schneller Energieboost"},
                {"name": "Dehnübungen", "time": "5 Min", "benefit": "Entspannt Muskulatur"}
            ],
            "🎵 Kreativ & Musikalisch": [
                {"name": "Lieblingslied singen", "time": "3-4 Min", "benefit": "Hebt Stimmung & reduziert Stress"},
                {"name": "Instrument spielen", "time": "5 Min", "benefit": "Aktiviert andere Gehirnareale"},
                {"name": "Summen & Tanzen", "time": "3 Min", "benefit": "Kombiniert Bewegung & Musik"}
            ],
            "🧘 Mind-Wandering": [
                {"name": "Tagträumen am Fenster", "time": "5 Min", "benefit": "Fördert Kreativität"},
                {"name": "Achtsamkeits-Spaziergang", "time": "10 Min", "benefit": "Reset für's Gehirn"},
                {"name": "Doodle/Kritzeln", "time": "5 Min", "benefit": "Entspannt & aktiviert"},
                {"name": "Mandala ausmalen", "time": "10 Min", "benefit": "Meditative Wirkung"}
            ],
            "🧠 Kognitive Erholung": [
                {"name": "Atemübung 4-7-8", "time": "3 Min", "benefit": "Beruhigt Nervensystem"},
                {"name": "Progressive Muskelentspannung", "time": "5 Min", "benefit": "Tiefe Entspannung"},
                {"name": "Visualisierung", "time": "5 Min", "benefit": "Mentale Erholung"},
                {"name": "Meditation", "time": "5-10 Min", "benefit": "Verbessert Fokus"}
            ]
        }
    
        # Zufällige Aktivität pro Kategorie
        for category, activities in pause_activities.items():
            with st.expander(category):
                activity = random.choice(activities)
                st.markdown(f"""
                <div style="background: #F0F9FF; padding: 1rem; border-radius: 10px; 
                            border-left: 4px solid #0EA5E9;">
                    <h4 style="margin: 0;">{activity['name']}</h4>
                    <p style="margin: 0.5rem 0;">⏱️ {activity['time']} | 
                    ✨ {activity['benefit']}</p>
                </div>
                """, unsafe_allow_html=True)
            
                if st.button(f"Diese Aktivität machen", key=f"act_{category}"):
                    st.session_state.pause_statistics["solo_pausen"] += 1
                    st.session_state.reward_stamps += 1
                    st.success("Super! +1 Stempel für deine aktive Pause!")

    # Lernstatistiken
    st.markdown("---")
    st.subheader("📊 Deine Lernstatistik heute")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Lernzeit gesamt", f"{st.session_state.total_learning_time} Min")
    with col2:
        st.metric("Abgeschlossene Intervalle", st.session_state.interval_count)
    with col3:
        focus_score = min(100, st.session_state.interval_count * 10)
        st.metric("Fokus-Score", f"{focus_score}%")
    with col4:
        st.metric("Produktive Pausen", st.session_state.pause_statistics["solo_pausen"])

    # Tipps für optimales Lernen
    with st.expander("💡 Tipps für optimales Lernen"):
        st.markdown("""
        **🧠 Gehirngerechtes Lernen:**
        - Nach 90 Min lässt die Konzentration natürlich nach
        - Kurze Pausen (5-10 Min) erhalten den Fokus
        - Lange Pausen (20-30 Min) ermöglichen Konsolidierung
    
        **🎯 Pausenqualität:**
        - Bewegung aktiviert das Gehirn neu
        - Tagträumen fördert kreative Lösungen
        - Meditation verbessert die nächste Lernphase
        - Handy-Pausen sind KEINE echten Pausen!
    
        **⚡ Energie-Management:**
        - Morgens: Schwierige, neue Inhalte
        - Mittags: Wiederholung, Übungen
        - Abends: Leichtes Review, Planung
        """)

    # Audio für Timer-Ende (optional)
    # Du kannst einen Ton abspielen wenn der Timer endet:
    def play_notification_sound():
        audio_html = """
        <audio autoplay>
            <source src="data:audio/wav;base64,UklGRnoGAABXQVZFZm10IBAAAAABAAEARKwAAIhYAQACABAAZGF0YQoGAACBhYqFbF1fdJivrJBhNjVgodDbq2EcBj+a2/LDciUFLIHO8tiJNwgZaLvt559NEAxQp+PwtmMcBjiR1/LMeSwFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBjiS1/LNeSsFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBj==")
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)


    

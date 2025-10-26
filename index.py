import React;
import { useState, useEffect, useRef } from 'react';
import { Heart, Music, BookOpen, TrendingUp, Play, Pause, Volume2, VolumeX, Clock, Calendar, Award, Sparkles, Star, Home } from 'lucide-react';
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const MEDITATION_TYPES = [
  { id: 'calm', name: 'Calm', icon: '🌊', color: 'bg-blue-100', description: 'Find inner peace' },
  { id: 'focus', name: 'Focus', icon: '🎯', color: 'bg-purple-100', description: 'Sharpen your mind' },
  { id: 'healing', name: 'Healing', icon: '💚', color: 'bg-green-100', description: 'Restore balance' },
  { id: 'awareness', name: 'Awareness', icon: '👁️', color: 'bg-yellow-100', description: 'Expand consciousness' },
  { id: 'gratitude', name: 'Gratitude', icon: '🙏', color: 'bg-pink-100', description: 'Cultivate thankfulness' },
  { id: 'balance', name: 'Balance', icon: '⚖️', color: 'bg-indigo-100', description: 'Find equilibrium' },
  { id: 'sleep', name: 'Sleep', icon: '🌙', color: 'bg-slate-100', description: 'Deep rest' },
  { id: 'energy', name: 'Energy Boost', icon: '⚡', color: 'bg-orange-100', description: 'Revitalize yourself' },
  { id: 'release', name: 'Emotional Release', icon: '🌸', color: 'bg-rose-100', description: 'Let go of tension' }
];

const MUSIC_TRACKS = [
  { id: 1, name: 'Ocean Waves', category: 'nature', emoji: '🌊' },
  { id: 2, name: 'Rainforest Ambience', category: 'nature', emoji: '🌧️' },
  { id: 3, name: 'Tibetan Singing Bowls', category: 'meditation', emoji: '🕉️' },
  { id: 4, name: 'Piano & Strings', category: 'instrumental', emoji: '🎹' },
  { id: 5, name: 'Wind & Birds', category: 'nature', emoji: '🌿' },
  { id: 6, name: 'Soft Rain', category: 'nature', emoji: '☔' },
  { id: 7, name: 'Crystal Bowls', category: 'meditation', emoji: '💎' },
  { id: 8, name: 'Forest Stream', category: 'nature', emoji: '🏞️' }
];

const AFFIRMATIONS = [
  "I am present in this moment",
  "Peace begins with me",
  "I trust the journey of my life",
  "Every breath brings calm",
  "I am worthy of inner peace",
  "My mind is clear and focused",
  "I release what I cannot control",
  "I am grateful for this moment",
  "Stillness is my natural state",
  "I honor my healing process"
];

const MOODS = [
  { emoji: '😊', label: 'Happy', value: 5 },
  { emoji: '😌', label: 'Calm', value: 4 },
  { emoji: '😐', label: 'Neutral', value: 3 },
  { emoji: '😟', label: 'Anxious', value: 2 },
  { emoji: '😢', label: 'Sad', value: 1 },
  { emoji: '🙏', label: 'Grateful', value: 5 }
];

const MEDITATION_GUIDES = {
  calm: {
    title: "Calm Meditation Guide",
    instructions: [
      "Find a comfortable seated position with your spine straight but relaxed",
      "Close your eyes gently or maintain a soft downward gaze",
      "Take three deep breaths - inhale through your nose, exhale through your mouth",
      "Let your breathing return to its natural rhythm",
      "Focus your attention on the sensation of breath at your nostrils or chest",
      "When your mind wanders (and it will), gently bring it back to your breath",
      "Notice the pause between inhale and exhale",
      "Allow any thoughts to pass like clouds in the sky",
      "Rest in the stillness between thoughts",
      "Feel the waves of calm washing over you with each exhale"
    ],
    mantra: "I am calm. I am peace. I am stillness."
  },
  focus: {
    title: "Focus Meditation Guide",
    instructions: [
      "Sit upright with alertness in your posture",
      "Choose a single point of focus - your breath, a candle flame, or a mantra",
      "Set your intention: 'I dedicate this time to developing concentration'",
      "Gently place your full attention on your chosen object",
      "Count your breaths from 1 to 10, then start again",
      "When distracted, acknowledge the thought and return to counting",
      "Strengthen your focus like training a muscle",
      "Notice when your mind is sharp versus dull",
      "Maintain steady, continuous awareness",
      "End by noticing your enhanced mental clarity"
    ],
    mantra: "One breath. One moment. One point of focus."
  },
  healing: {
    title: "Healing Meditation Guide",
    instructions: [
      "Settle into a position that feels nurturing and safe",
      "Place one hand on your heart, one on your belly",
      "Breathe deeply into your hands, feeling them rise and fall",
      "Visualize a warm, golden light at your heart center",
      "With each inhale, draw in healing energy",
      "With each exhale, release pain, tension, and what no longer serves you",
      "Let the golden light expand through your entire body",
      "Send healing energy to any area that needs it",
      "Acknowledge your wounds with compassion",
      "Affirm: 'I am healing. I am whole. I am enough.'"
    ],
    mantra: "Every breath heals me. Every moment restores me."
  },
  awareness: {
    title: "Awareness Meditation Guide",
    instructions: [
      "Sit in a position of dignified presence",
      "Open your awareness like the vast sky",
      "Notice whatever arises - sounds, sensations, thoughts, emotions",
      "Don't focus on anything specifically; remain open to everything",
      "Observe without labeling or judging",
      "Notice the spacious awareness that contains all experiences",
      "Recognize that you are the awareness, not the content",
      "Expand your consciousness beyond the boundaries of your body",
      "Rest as pure witnessing presence",
      "Simply be aware that you are aware"
    ],
    mantra: "I am the witness. I am consciousness itself."
  },
  gratitude: {
    title: "Gratitude Meditation Guide",
    instructions: [
      "Settle into your seat with a gentle smile",
      "Place your hands over your heart",
      "Take a moment to feel the gift of this breath",
      "Bring to mind three things you're grateful for today",
      "Really feel the appreciation in your body",
      "Thank your body for carrying you through life",
      "Appreciate someone who has helped you",
      "Feel gratitude for challenges that helped you grow",
      "Extend thanks to the air you breathe, the earth beneath you",
      "Let your heart overflow with appreciation for this precious life"
    ],
    mantra: "Thank you. I am grateful. I am blessed."
  },
  balance: {
    title: "Balance Meditation Guide",
    instructions: [
      "Find your center - physically and mentally",
      "Notice the balance between effort and ease in your posture",
      "Breathe equally through both nostrils if possible",
      "Visualize yourself as a mountain - stable yet flexible",
      "Acknowledge both light and shadow within you",
      "Balance acceptance with aspiration",
      "Honor rest as much as action",
      "Find equilibrium between giving and receiving",
      "Notice the still point at the center of all movement",
      "Rest in the balance of being"
    ],
    mantra: "I am centered. I am balanced. I am whole."
  },
  sleep: {
    title: "Sleep Meditation Guide",
    instructions: [
      "Lie down in a comfortable position for sleep",
      "Let your body sink into the surface beneath you",
      "Take several deep, slow breaths, releasing tension with each exhale",
      "Progressively relax each part of your body from head to toes",
      "Let go of the day - all tasks, worries, and thoughts",
      "Imagine yourself floating on calm, warm water",
      "With each breath, drift deeper into relaxation",
      "Allow thoughts to dissolve like mist",
      "Trust that sleep will come naturally",
      "Surrender completely to rest"
    ],
    mantra: "I release the day. I welcome deep, peaceful sleep."
  },
  energy: {
    title: "Energy Boost Meditation Guide",
    instructions: [
      "Sit upright with an energized posture",
      "Take several quick, energizing breaths (breath of fire)",
      "Visualize bright, vibrant light entering your body",
      "Feel energy gathering at your solar plexus",
      "With each inhale, draw in vitality and life force",
      "Imagine roots growing from your feet, drawing energy from the earth",
      "Feel your spine as a channel of flowing energy",
      "Clench and release your fists to activate your body",
      "Affirm your strength and vitality",
      "End with lion's breath - exhale forcefully with tongue out"
    ],
    mantra: "I am alive. I am energized. I am powerful."
  },
  release: {
    title: "Emotional Release Meditation Guide",
    instructions: [
      "Find a private space where you can express freely",
      "Allow yourself to feel whatever emotions are present",
      "Take deep breaths into the center of the emotion",
      "Don't suppress or judge - just feel and observe",
      "Visualize the emotion as a color or energy",
      "With each exhale, imagine releasing this energy",
      "You might cry, shake, or feel waves of sensation - this is healing",
      "Place your hands on any area holding tension",
      "Speak or write what needs to be expressed",
      "Conclude by filling the space with light and peace"
    ],
    mantra: "I release what no longer serves me. I am free."
  }
};

const LEARN_CONTENT = [
  {
    title: "How Meditation Calms the Nervous System",
    description: "Understanding the science behind mindful breathing and stress reduction",
    category: "Science",
    icon: "🧠",
    fullContent: `Meditation activates the parasympathetic nervous system, which is responsible for the body "rest and digest" response. When you meditate:

 "Your heart rate slows down"
 "Blood pressure decreases"
 "Stress hormones like cortisol are reduced"
 "The amygdala (fear center) becomes less reactive"
 "The prefrontal cortex (reasoning center) becomes more active"

Regular practice can actually change the structure of your brain, increasing gray matter in areas associated with emotional regulation, learning, and memory. Even 10 minutes a day can make a significant difference in how your nervous system responds to stress.`
  },
  {
    title: "Self-Realization through Chakra Meditation",
    description: "Ancient practices for balancing your energy centers",
    category: "Spiritual",
    icon: "🕉️",
    fullContent: `The chakra system represents seven energy centers in your body, from the base of your spine to the crown of your head:

1. Root Chakra (Muladhara) - Grounding and survival
2. Sacral Chakra (Svadhisthana) - Creativity and emotions
3. Solar Plexus (Manipura) - Personal power and confidence
4. Heart Chakra (Anahata) - Love and compassion
5. Throat Chakra (Vishuddha) - Communication and truth
6. Third Eye (Ajna) - Intuition and insight
7. Crown Chakra (Sahasrara) - Spiritual connection

To practice: Sit comfortably, focus on each chakra location, visualize its associated color, and breathe into that area. Notice any sensations, emotions, or blockages.`
  },
  {
    title: "Grounding Techniques for Anxiety",
    description: "Quick exercises to return to the present moment",
    category: "Practice",
    icon: "🌱",
    fullContent: `When anxiety strikes, these grounding techniques can bring you back to the present:

5-4-3-2-1 Method:
 "Name 5 things you can see"
 "4 things you can touch"
 "3 things you can hear"
 "2 things you can smell"
 "1 thing you can taste"

Physical Grounding:
 "Press your feet firmly into the floor"
 "Hold ice cubes in your hands"
 "Splash cold water on your face"
 "Do progressive muscle relaxation"`
  },
  {
    title: "The Art of Body Scan Meditation",
    description: "Progressive relaxation for deep healing",
    category: "Technique",
    icon: "✨",
    fullContent: `Body scan meditation is a systematic way to release tension and develop body awareness:

How to Practice:
1. Lie down or sit comfortably
2. Close your eyes and take several deep breaths
3. Start at the top of your head
4. Slowly move attention down through each body part
5. Notice sensations without judgment
6. Breathe into areas of tension
7. Continue down to your toes

Practice for 10-30 minutes daily.`
  },
  {
    title: "Loving-Kindness Meditation",
    description: "Cultivate compassion for yourself and others",
    category: "Heart",
    icon: "💗",
    fullContent: `Loving-kindness (Metta) meditation develops unconditional love and compassion:

Phrases to repeat:
 1. May I/you be safe
 2. May I/you be healthy
 3. May I/you be happy
 4. May I/you live with ease

Begin with yourself, then extend to loved ones, neutral people, difficult people, and all beings.`
  }
];

class AmbientSoundEngine {
  constructor() {
    this.audioContext = null;
    this.oscillators = [];
    this.gainNodes = [];
    this.isPlaying = false;
  }
  
  init() {
    if (!this.audioContext) {
      this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
    }
  }
  
  play(trackType) {
    this.init();
    this.stop();
    
    const masterGain = this.audioContext.createGain();
    masterGain.gain.value = 0.3;
    masterGain.connect(this.audioContext.destination);
    
    if (trackType === 1) {
      this.createOceanWaves(masterGain);
    } else if (trackType === 2 || trackType === 6) {
      this.createRain(masterGain);
    } else if (trackType === 3 || trackType === 7) {
      this.createSingingBowls(masterGain);
    } else if (trackType === 5 || trackType === 8) {
      this.createWind(masterGain);
    } else {
      this.createCalm(masterGain);
    }
    
    this.isPlaying = true;
  }
  
  createOceanWaves(destination) {
    const bufferSize = 4096;
    const whiteNoise = this.audioContext.createScriptProcessor(bufferSize, 1, 1);
    whiteNoise.onaudioprocess = (e) => {
      const output = e.outputBuffer.getChannelData(0);
      for (let i = 0; i < bufferSize; i++) {
        output[i] = Math.random() * 2 - 1;
      }
    };
    
    const filter = this.audioContext.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.value = 800;
    
    const gainNode = this.audioContext.createGain();
    gainNode.gain.value = 0.5;
    
    whiteNoise.connect(filter);
    filter.connect(gainNode);
    gainNode.connect(destination);
    
    this.oscillators.push(whiteNoise);
    this.gainNodes.push(gainNode);
  }
  
  createRain(destination) {
    const bufferSize = 2048;
    const whiteNoise = this.audioContext.createScriptProcessor(bufferSize, 1, 1);
    whiteNoise.onaudioprocess = (e) => {
      const output = e.outputBuffer.getChannelData(0);
      for (let i = 0; i < bufferSize; i++) {
        output[i] = Math.random() * 2 - 1;
      }
    };
    
    const filter = this.audioContext.createBiquadFilter();
    filter.type = 'bandpass';
    filter.frequency.value = 2000;
    
    const gainNode = this.audioContext.createGain();
    gainNode.gain.value = 0.4;
    
    whiteNoise.connect(filter);
    filter.connect(gainNode);
    gainNode.connect(destination);
    
    this.oscillators.push(whiteNoise);
    this.gainNodes.push(gainNode);
  }
  
  createSingingBowls(destination) {
    const frequencies = [256, 384, 512, 768];
    
    frequencies.forEach((freq, idx) => {
      const osc = this.audioContext.createOscillator();
      osc.type = 'sine';
      osc.frequency.value = freq;
      
      const gainNode = this.audioContext.createGain();
      gainNode.gain.value = 0;
      
      osc.connect(gainNode);
      gainNode.connect(destination);
      osc.start();
      
      const now = this.audioContext.currentTime;
      const interval = 8 + idx * 2;
      
      gainNode.gain.setValueAtTime(0, now);
      gainNode.gain.linearRampToValueAtTime(0.15, now + 2);
      gainNode.gain.exponentialRampToValueAtTime(0.01, now + interval);
      
      this.oscillators.push(osc);
      this.gainNodes.push(gainNode);
    });
  }
  
  createWind(destination) {
    const bufferSize = 4096;
    const whiteNoise = this.audioContext.createScriptProcessor(bufferSize, 1, 1);
    whiteNoise.onaudioprocess = (e) => {
      const output = e.outputBuffer.getChannelData(0);
      for (let i = 0; i < bufferSize; i++) {
        output[i] = Math.random() * 2 - 1;
      }
    };
    
    const filter = this.audioContext.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.value = 1200;
    
    const gainNode = this.audioContext.createGain();
    gainNode.gain.value = 0.3;
    
    whiteNoise.connect(filter);
    filter.connect(gainNode);
    gainNode.connect(destination);
    
    this.oscillators.push(whiteNoise);
    this.gainNodes.push(gainNode);
  }
  
  createCalm(destination) {
    [200, 300, 400].forEach((freq) => {
      const osc = this.audioContext.createOscillator();
      osc.type = 'sine';
      osc.frequency.value = freq;
      
      const gainNode = this.audioContext.createGain();
      gainNode.gain.value = 0.08;
      
      osc.connect(gainNode);
      gainNode.connect(destination);
      osc.start();
      
      this.oscillators.push(osc);
      this.gainNodes.push(gainNode);
    });
  }
  
  setVolume(volume) {
    this.gainNodes.forEach(gain => {
      gain.gain.value = volume * 0.5;
    });
  }
  
  stop() {
    this.oscillators.forEach(osc => {
      try {
        if (osc.stop) osc.stop();
        if (osc.disconnect) osc.disconnect();
      } catch (e) {}
    });
    this.oscillators = [];
    this.gainNodes = [];
    this.isPlaying = false;
  }
}

const analyzeSentiment = (text) => {
  const positive = ['happy', 'peaceful', 'calm', 'grateful', 'joy', 'love', 'good', 'better', 'clear', 'light'];
  const negative = ['anxious', 'stressed', 'sad', 'tired', 'overwhelmed', 'worried', 'pain', 'difficult', 'heavy'];
  
  const words = text.toLowerCase().split(/\s+/);
  let score = 3;
  
  words.forEach(word => {
    if (positive.some(p => word.includes(p))) score += 0.5;
    if (negative.some(n => word.includes(n))) score -= 0.5;
  });
  
  return Math.max(1, Math.min(5, score));
};

const getRecommendation = (sessions, journals) => {
  if (sessions.length === 0) {
    return {
      type: 'calm',
      message: "Welcome to your mindfulness journey. Let's start with a calming session to center yourself."
    };
  }
  
  const recentMoods = sessions.slice(-5).map(s => s.moodBefore);
  const avgMood = recentMoods.reduce((a, b) => a + b, 0) / recentMoods.length;
  
  if (avgMood < 2.5) {
    return { type: 'healing', message: "I sense you've been carrying some weight. A healing session might help you release and restore." };
  } else if (avgMood < 3) {
    return { type: 'calm', message: "You've felt anxious lately. Let's cultivate some calm together." };
  } else {
    return { type: 'balance', message: "Maintain your equilibrium with a balanced meditation today." };
  }
};

export default function SukoonApp() {
  const [currentView, setCurrentView] = useState('home');
  const [username, setUsername] = useState('');
  const [showNamePrompt, setShowNamePrompt] = useState(true);
  const [sessions, setSessions] = useState([]);
  const [journals, setJournals] = useState([]);
  const [currentAffirmation, setCurrentAffirmation] = useState('');
  const [musicPlaying, setMusicPlaying] = useState(false);
  const [musicVolume, setMusicVolume] = useState(0.5);
  const [currentTrack, setCurrentTrack] = useState(MUSIC_TRACKS[0]);
  const [bookmarkedContent, setBookmarkedContent] = useState([]);
  const soundEngine = useRef(null);
  
  useEffect(() => {
    loadUserData();
    soundEngine.current = new AmbientSoundEngine();
    
    return () => {
      if (soundEngine.current) {
        soundEngine.current.stop();
      }
    };
  }, []);
  
  useEffect(() => {
    if (soundEngine.current) {
      if (musicPlaying) {
        soundEngine.current.play(currentTrack.id);
        soundEngine.current.setVolume(musicVolume);
      } else {
        soundEngine.current.stop();
      }
    }
  }, [musicPlaying, currentTrack]);
  
  useEffect(() => {
    if (soundEngine.current && musicPlaying) {
      soundEngine.current.setVolume(musicVolume);
    }
  }, [musicVolume]);
  
  const loadUserData = async () => {
    try {
      const userResult = await window.storage.get('sukoon-user');
      if (userResult) {
        const userData = JSON.parse(userResult.value);
        setUsername(userData.username);
        setShowNamePrompt(false);
      }
      
      const sessionsResult = await window.storage.get('sukoon-sessions');
      if (sessionsResult) setSessions(JSON.parse(sessionsResult.value));
      
      const journalsResult = await window.storage.get('sukoon-journals');
      if (journalsResult) setJournals(JSON.parse(journalsResult.value));
      
      const bookmarksResult = await window.storage.get('sukoon-bookmarks');
      if (bookmarksResult) setBookmarkedContent(JSON.parse(bookmarksResult.value));
    } catch (error) {
      console.log('First time user');
    }
    
    setCurrentAffirmation(AFFIRMATIONS[Math.floor(Math.random() * AFFIRMATIONS.length)]);
  };
  
  const saveUsername = async (name) => {
    setUsername(name);
    setShowNamePrompt(false);
    try {
      await window.storage.set('sukoon-user', JSON.stringify({ username: name }));
    } catch (error) {
      console.error('Error:', error);
    }
  };
  
  const saveSession = async (sessionData) => {
    const newSessions = [...sessions, { ...sessionData, id: Date.now(), date: new Date().toISOString() }];
    setSessions(newSessions);
    try {
      await window.storage.set('sukoon-sessions', JSON.stringify(newSessions));
    } catch (error) {
      console.error('Error:', error);
    }
  };
  
  const saveJournal = async (journalData) => {
    const newJournals = [...journals, { ...journalData, id: Date.now(), date: new Date().toISOString() }];
    setJournals(newJournals);
    try {
      await window.storage.set('sukoon-journals', JSON.stringify(newJournals));
    } catch (error) {
      console.error('Error:', error);
    }
  };
  
  const toggleBookmark = async (content) => {
    const isBookmarked = bookmarkedContent.some(b => b.title === content.title);
    const newBookmarks = isBookmarked
      ? bookmarkedContent.filter(b => b.title !== content.title)
      : [...bookmarkedContent, content];
    
    setBookmarkedContent(newBookmarks);
    try {
      await window.storage.set('sukoon-bookmarks', JSON.stringify(newBookmarks));
    } catch (error) {
      console.error('Error:', error);
    }
  };
  
  const getGreeting = () => {
    const hour = new Date().getHours();
    if (hour < 12) return '🌅 Good Morning';
    if (hour < 17) return '☀️ Good Afternoon';
    if (hour < 21) return '🌆 Good Evening';
    return '🌙 Good Night';
  };
  
  if (showNamePrompt) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-green-50 via-purple-50 to-blue-50 flex items-center justify-center p-4">
        <div className="bg-white rounded-3xl shadow-xl p-8 max-w-md w-full">
          <div className="text-center mb-6">
            <div className="text-6xl mb-4">🪷</div>
            <h1 className="text-4xl font-serif text-slate-800 mb-2">Sukoon</h1>
            <p className="text-slate-600">Your sanctuary of peace</p>
          </div>
          <div>
            <label className="block text-slate-700 mb-2">What should we call you?</label>
            <input
              type="text"
              placeholder="Enter your name"
              className="w-full px-4 py-3 rounded-xl border-2 border-slate-200 focus:border-purple-400 focus:outline-none"
              onKeyPress={(e) => {
                if (e.key === 'Enter' && e.target.value.trim()) {
                  saveUsername(e.target.value.trim());
                }
              }}
            />
            <button
              onClick={(e) => {
                const input = e.target.previousElementSibling;
                if (input.value.trim()) saveUsername(input.value.trim());
              }}
              className="w-full mt-4 bg-gradient-to-r from-purple-500 to-blue-500 text-white py-3 rounded-xl hover:shadow-lg transition-all"
            >
              Begin Your Journey
            </button>
          </div>
        </div>
      </div>
    );
  }
  
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-purple-50 to-blue-50">
      {currentView === 'home' && <HomeView 
        username={username}
        greeting={getGreeting()}
        affirmation={currentAffirmation}
        setCurrentView={setCurrentView}
        musicPlaying={musicPlaying}
        setMusicPlaying={setMusicPlaying}
        sessions={sessions}
        journals={journals}
        musicVolume={musicVolume}
        setMusicVolume={setMusicVolume}
        currentTrack={currentTrack}
        setCurrentTrack={setCurrentTrack}
      />}
      
      {currentView === 'meditation' && <MeditationFlow 
        setCurrentView={setCurrentView}
        saveSession={saveSession}
        saveJournal={saveJournal}
        currentTrack={currentTrack}
        setCurrentTrack={setCurrentTrack}
        musicPlaying={musicPlaying}
        setMusicPlaying={setMusicPlaying}
        musicVolume={musicVolume}
        setMusicVolume={setMusicVolume}
        sessions={sessions}
        journals={journals}
      />}
      
      {currentView === 'journal' && <JournalView 
        setCurrentView={setCurrentView}
        journals={journals}
        saveJournal={saveJournal}
      />}
      
      {currentView === 'progress' && <ProgressView 
        setCurrentView={setCurrentView}
        sessions={sessions}
        journals={journals}
      />}
      
      {currentView === 'discover' && <DiscoverView 
        setCurrentView={setCurrentView}
        bookmarkedContent={bookmarkedContent}
        toggleBookmark={toggleBookmark}
      />}
    </div>
  );
}

function HomeView({ username, greeting, affirmation, setCurrentView, musicPlaying, setMusicPlaying, sessions, journals, musicVolume, setMusicVolume, currentTrack, setCurrentTrack }) {
  const recommendation = getRecommendation(sessions, journals);
  
  return (
    <div className="max-w-6xl mx-auto p-6">
      <header className="text-center mb-12 relative">
        <div className="absolute top-0 right-0">
          <img src="https://i.imgur.com/8qZ5K9M.png" alt="Amity University" className="h-16 w-16 object-contain" />
        </div>
        <div className="text-5xl mb-4">🪷</div>
        <h1 className="text-5xl font-serif text-slate-800 mb-2">Sukoon</h1>
        <p className="text-xl text-slate-600">{greeting}, {username}</p>
      </header>
      
      <div className="bg-white/80 backdrop-blur rounded-3xl p-8 mb-8 shadow-lg">
        <div className="flex items-center gap-3 mb-4">
          <Sparkles className="text-purple-500" size={24} />
          <h3 className="text-lg font-medium text-slate-700">Today's Mindful Insight</h3>
        </div>
        <p className="text-2xl font-serif text-slate-800 italic">"{affirmation}"</p>
      </div>
      
      {sessions.length > 0 && (
        <div className="bg-gradient-to-r from-purple-100 to-blue-100 rounded-3xl p-6 mb-8">
          <div className="flex items-center gap-3 mb-3">
            <Sparkles className="text-purple-600" size={20} />
            <h3 className="text-lg font-medium text-slate-800">AI Suggestion for You</h3>
          </div>
          <p className="text-slate-700">{recommendation.message}</p>
        </div>
      )}
      
      <div className="grid md:grid-cols-2 gap-6">
        <NavCard
          icon={<Play size={32} />}
          title="Start Meditation"
          description="Begin your practice"
          color="from-blue-400 to-purple-500"
          onClick={() => setCurrentView('meditation')}
        />
        <NavCard
          icon={<BookOpen size={32} />}
          title="My Journal"
          description="Reflect and grow"
          color="from-green-400 to-teal-500"
          onClick={() => setCurrentView('journal')}
        />
        <NavCard
          icon={<TrendingUp size={32} />}
          title="My Progress"
          description="Track your journey"
          color="from-purple-400 to-pink-500"
          onClick={() => setCurrentView('progress')}
        />
        <NavCard
          icon={<Heart size={32} />}
          title="Discover & Learn"
          description="Expand your practice"
          color="from-orange-400 to-red-500"
          onClick={() => setCurrentView('discover')}
        />
      </div>
      
      <div className="mt-8 text-center">
        <button
          onClick={() => setMusicPlaying(!musicPlaying)}
          className="inline-flex items-center gap-2 px-6 py-3 bg-white rounded-full shadow-md hover:shadow-lg transition-all"
        >
          {musicPlaying ? <Pause size={20} /> : <Play size={20} />}
          <span>{musicPlaying ? 'Pause' : 'Play'} Ambient Sound</span>
          <Music size={16} className="text-purple-500" />
        </button>
        
        {musicPlaying && (
          <div className="mt-4 flex items-center gap-3 justify-center flex-wrap">
            <div className="flex items-center gap-2">
              <VolumeX size={16} className="text-slate-400" />
              <input
                type="range"
                min="0"
                max="1"
                step="0.1"
                value={musicVolume}
                onChange={(e) => setMusicVolume(parseFloat(e.target.value))}
                className="w-32"
              />
              <Volume2 size={16} className="text-slate-600" />
            </div>
            <select
              value={currentTrack.id}
              onChange={(e) => {
                const track = MUSIC_TRACKS.find(t => t.id === parseInt(e.target.value));
                setCurrentTrack(track);
              }}
              className="px-4 py-2 bg-white rounded-xl border-2 border-slate-200"
            >
              {MUSIC_TRACKS.map(track => (
                <option key={track.id} value={track.id}>
                  {track.emoji} {track.name}
                </option>
              ))}
            </select>
          </div>
        )}
      </div>
    </div>
  );
}

function NavCard({ icon, title, description, color, onClick }) {
  return (
    <button
      onClick={onClick}
      className={`bg-gradient-to-br ${color} p-8 rounded-3xl text-white text-left hover:scale-105 transition-transform shadow-lg`}
    >
      <div className="mb-4">{icon}</div>
      <h3 className="text-2xl font-semibold mb-2">{title}</h3>
      <p className="text-white/90">{description}</p>
    </button>
  );
}

function MeditationFlow({ setCurrentView, saveSession, saveJournal, currentTrack, setCurrentTrack, musicPlaying, setMusicPlaying, musicVolume, setMusicVolume, sessions, journals }) {
  const [step, setStep] = useState('setup');
  const [duration, setDuration] = useState(5);
  const [selectedType, setSelectedType] = useState(null);
  const [prePrompts, setPrePrompts] = useState({ bringing: '', feeling: '', intention: '' });
  const [moodBefore, setMoodBefore] = useState(3);
  const [timeLeft, setTimeLeft] = useState(0);
  const [isActive, setIsActive] = useState(false);
  const [postPrompts, setPostPrompts] = useState({ feelingNow: '', emotions: '', oneWord: '' });
  const [moodAfter, setMoodAfter] = useState(3);
  const [currentInstruction, setCurrentInstruction] = useState(0);
  const timerRef = useRef(null);
  
  useEffect(() => {
    if (isActive && timeLeft > 0) {
      timerRef.current = setInterval(() => {
        setTimeLeft(t => t - 1);
      }, 1000);
    } else if (timeLeft === 0 && isActive) {
      setIsActive(false);
      setMusicPlaying(false);
      setStep('post');
    }
    return () => clearInterval(timerRef.current);
  }, [isActive, timeLeft]);
  
  useEffect(() => {
    if (step === 'active' && selectedType) {
      const guide = MEDITATION_GUIDES[selectedType.id];
      const instructionInterval = setInterval(() => {
        setCurrentInstruction(prev => (prev + 1) % guide.instructions.length);
      }, 30000);
      
      return () => clearInterval(instructionInterval);
    }
  }, [step, selectedType]);
  
  const startSession = () => {
    setTimeLeft(duration * 60);
    setIsActive(true);
    setMusicPlaying(true);
    setStep('active');
    setCurrentInstruction(0);
  };
  
  const completeSession = () => {
    const sessionData = {
      type: selectedType.id,
      duration,
      moodBefore,
      moodAfter,
      prePrompts,
      postPrompts
    };
    saveSession(sessionData);
    
    const journalEntry = {
      type: selectedType.name,
      moodBefore,
      moodAfter,
      reflection: `${postPrompts.feelingNow} ${postPrompts.emotions} ${postPrompts.oneWord}`,
      tags: [selectedType.id]
    };
    saveJournal(journalEntry);
    
    setCurrentView('home');
  };
  
  const recommendation = getRecommendation(sessions, journals);
  
  if (step === 'setup') {
    return (
      <div className="max-w-4xl mx-auto p-6">
        <button onClick={() => setCurrentView('home')} className="mb-6 text-slate-600 hover:text-slate-800 flex items-center gap-2">
          <Home size={20} /> Back to Home
        </button>
        
        <h2 className="text-4xl font-serif text-slate-800 mb-8">Prepare Your Practice</h2>
        
        {sessions.length > 0 && (
          <div className="bg-purple-50 rounded-2xl p-6 mb-8">
            <p className="text-slate-700"><span className="text-2xl">💡</span> <strong>Suggested:</strong> {recommendation.message}</p>
          </div>
        )}
        
        <div className="mb-8">
          <label className="block text-slate-700 mb-3 text-lg">Duration (minutes)</label>
          <input
            type="range"
            min="1"
            max="60"
            value={duration}
            onChange={(e) => setDuration(parseInt(e.target.value))}
            className="w-full"
          />
          <div className="text-center text-3xl font-semibold text-purple-600 mt-2">{duration} min</div>
        </div>
        
        <div className="mb-8">
          <label className="block text-slate-700 mb-3 text-lg">Choose Your Practice</label>
          <div className="grid grid-cols-3 gap-4">
            {MEDITATION_TYPES.map(type => (
              <button
                key={type.id}
                onClick={() => setSelectedType(type)}
                className={`${type.color} p-4 rounded-2xl text-center transition-all ${
                  selectedType?.id === type.id ? 'ring-4 ring-purple-500 scale-105' : ''
                }`}
              >
                <div className="text-4xl mb-2">{type.icon}</div>
                <div className="font-semibold text-slate-800">{type.name}</div>
                <div className="text-sm text-slate-600">{type.description}</div>
              </button>
            ))}
          </div>
        </div>
        
        {selectedType && (
          <button
            onClick={() => setStep('pre')}
            className="w-full bg-gradient-to-r from-purple-500 to-blue-500 text-white py-4 rounded-2xl text-lg font-semibold hover:shadow-xl transition-all"
          >
            Continue
          </button>
        )}
      </div>
    );
  }
  
  if (step === 'pre') {
    return (
      <div className="max-w-2xl mx-auto p-6">
        <button onClick={() => setStep('setup')} className="mb-6 text-slate-600 hover:text-slate-800">
          ← Back
        </button>
        
        <h2 className="text-3xl font-serif text-slate-800 mb-8">Before We Begin</h2>
        
        <div className="space-y-6">
          <div>
            <label className="block text-slate-700 mb-2">What brings you here today?</label>
            <textarea
              value={prePrompts.bringing}
              onChange={(e) => setPrePrompts({...prePrompts, bringing: e.target.value})}
              className="w-full p-4 rounded-xl border-2 border-slate-200 focus:border-purple-400 focus:outline-none"
              rows="3"
            />
          </div>
          
          <div>
            <label className="block text-slate-700 mb-2">How do you feel right now?</label>
            <div className="flex gap-4 justify-center my-4 flex-wrap">
              {MOODS.map(mood => (
                <button
                  key={mood.label}
                  onClick={() => setMoodBefore(mood.value)}
                  className={`text-4xl p-3 rounded-2xl transition-all ${
                    moodBefore === mood.value ? 'bg-purple-100 scale-125' : 'hover:scale-110'
                  }`}
                  title={mood.label}
                >
                  {mood.emoji}
                </button>
              ))}
            </div>
          </div>
          
          <div>
            <label className="block text-slate-700 mb-2">What would you like to release or invite?</label>
            <textarea
              value={prePrompts.intention}
              onChange={(e) => setPrePrompts({...prePrompts, intention: e.target.value})}
              className="w-full p-4 rounded-xl border-2 border-slate-200 focus:border-purple-400 focus:outline-none"
              rows="3"
            />
          </div>
        </div>
        
        <button
          onClick={startSession}
          className="w-full mt-8 bg-gradient-to-r from-green-500 to-blue-500 text-white py-4 rounded-2xl text-lg font-semibold hover:shadow-xl transition-all"
        >
          Begin Session
        </button>
      </div>
    );
  }
  
  if (step === 'active') {
    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;
    const guide = MEDITATION_GUIDES[selectedType.id];
    
    return (
      <div className="min-h-screen flex flex-col items-center justify-center p-6 bg-gradient-to-br from-indigo-900 via-purple-900 to-blue-900">
        <style>
          {`
            @keyframes breathe {
              0%, 100% { transform: scale(1); opacity: 0.5; }
              50% { transform: scale(1.2); opacity: 0.8; }
            }
            .breathing-circle {
              animation: breathe 6s ease-in-out infinite;
            }
            @keyframes fadeInOut {
              0%, 100% { opacity: 0.5; }
              50% { opacity: 1; }
            }
            .breathing-text {
              animation: fadeInOut 6s ease-in-out infinite;
            }
            @keyframes slideUp {
              from { opacity: 0; transform: translateY(20px); }
              to { opacity: 1; transform: translateY(0); }
            }
            .instruction-text {
              animation: slideUp 1s ease-out;
            }
          `}
        </style>
        <div className="text-center max-w-3xl">
          <div className="mb-8">
            <div className="text-6xl mb-4">{selectedType.icon}</div>
            <h2 className="text-3xl font-serif text-white mb-2">{guide.title}</h2>
            <p className="text-white/70">{selectedType.description}</p>
          </div>
          
          <div className="mb-8">
            <div className="breathing-circle w-48 h-48 mx-auto rounded-full bg-white/10 backdrop-blur flex items-center justify-center">
              <div className="text-6xl font-light text-white">
                {minutes}:{seconds.toString().padStart(2, '0')}
              </div>
            </div>
          </div>
          
          <div className="mb-8 min-h-32">
            <div className="breathing-text text-xl text-white/80 mb-4">
              Breathe in... and out...
            </div>
            <div className="instruction-text bg-white/5 backdrop-blur rounded-2xl p-6 mx-auto max-w-2xl">
              <p className="text-white/90 text-lg leading-relaxed">
                {guide.instructions[currentInstruction]}
              </p>
              <div className="mt-4 flex gap-1 justify-center">
                {guide.instructions.map((_, idx) => (
                  <div
                    key={idx}
                    className={`h-1 w-8 rounded-full transition-all ${
                      idx === currentInstruction ? 'bg-white' : 'bg-white/30'
                    }`}
                  />
                ))}
              </div>
            </div>
            <p className="text-white/60 italic mt-4 text-sm">{guide.mantra}</p>
          </div>
          
          <div className="flex gap-4 justify-center mb-6">
            <button
              onClick={() => setMusicPlaying(!musicPlaying)}
              className="p-4 bg-white/10 backdrop-blur rounded-full hover:bg-white/20 transition-all"
            >
              {musicPlaying ? <Pause className="text-white" /> : <Play className="text-white" />}
            </button>
            
            <button
              onClick={() => {
                setIsActive(false);
                setMusicPlaying(false);
                setStep('post');
              }}
              className="px-6 py-3 bg-white/10 backdrop-blur rounded-full text-white hover:bg-white/20 transition-all"
            >
              End Early
            </button>
          </div>
          
          <div className="mt-6">
            <div className="flex items-center gap-4 justify-center mb-3">
              <label className="text-white/80 text-sm">Background Sound:</label>
              <select
                value={currentTrack.id}
                onChange={(e) => {
                  const track = MUSIC_TRACKS.find(t => t.id === parseInt(e.target.value));
                  setCurrentTrack(track);
                }}
                className="px-4 py-2 bg-white/10 backdrop-blur text-white rounded-xl border border-white/20 text-sm"
              >
                {MUSIC_TRACKS.map(track => (
                  <option key={track.id} value={track.id} className="text-slate-800">
                    {track.emoji} {track.name}
                  </option>
                ))}
              </select>
            </div>
            
            <div className="flex items-center gap-3 justify-center">
              <VolumeX size={16} className="text-white/60" />
              <input
                type="range"
                min="0"
                max="1"
                step="0.1"
                value={musicVolume}
                onChange={(e) => setMusicVolume(parseFloat(e.target.value))}
                className="w-32"
              />
              <Volume2 size={16} className="text-white" />
            </div>
          </div>
        </div>
      </div>
    );
  }
  
  if (step === 'post') {
    return (
      <div className="max-w-2xl mx-auto p-6">
        <h2 className="text-3xl font-serif text-slate-800 mb-8">Reflection Time</h2>
        
        <div className="bg-green-50 rounded-2xl p-6 mb-8 text-center">
          <div className="text-5xl mb-3">✨</div>
          <p className="text-xl text-slate-700">Session Complete!</p>
        </div>
        
        <div className="space-y-6">
          <div>
            <label className="block text-slate-700 mb-2">How do you feel now?</label>
            <div className="flex gap-4 justify-center my-4 flex-wrap">
              {MOODS.map(mood => (
                <button
                  key={mood.label}
                  onClick={() => setMoodAfter(mood.value)}
                  className={`text-4xl p-3 rounded-2xl transition-all ${
                    moodAfter === mood.value ? 'bg-green-100 scale-125' : 'hover:scale-110'
                  }`}
                  title={mood.label}
                >
                  {mood.emoji}
                </button>
              ))}
            </div>
          </div>
          
          <div>
            <label className="block text-slate-700 mb-2">What emotions surfaced during the session?</label>
            <textarea
              value={postPrompts.emotions}
              onChange={(e) => setPostPrompts({...postPrompts, emotions: e.target.value})}
              className="w-full p-4 rounded-xl border-2 border-slate-200 focus:border-green-400 focus:outline-none"
              rows="3"
              placeholder="Describe what came up for you..."
            />
          </div>
          
          <div>
            <label className="block text-slate-700 mb-2">One word to describe your mind right now</label>
            <input
              type="text"
              value={postPrompts.oneWord}
              onChange={(e) => setPostPrompts({...postPrompts, oneWord: e.target.value})}
              className="w-full p-4 rounded-xl border-2 border-slate-200 focus:border-green-400 focus:outline-none"
              placeholder="e.g., peaceful, clear, light..."
            />
          </div>
        </div>
        
        <button
          onClick={completeSession}
          className="w-full mt-8 bg-gradient-to-r from-green-500 to-teal-500 text-white py-4 rounded-2xl text-lg font-semibold hover:shadow-xl transition-all"
        >
          Complete & Save
        </button>
      </div>
    );
  }
  
  return null;
}

function JournalView({ setCurrentView, journals, saveJournal }) {
  const [showNewEntry, setShowNewEntry] = useState(false);
  const [newEntry, setNewEntry] = useState({ reflection: '', mood: 3, tags: [] });
  
  const handleSaveEntry = () => {
    if (newEntry.reflection.trim()) {
      saveJournal({
        ...newEntry,
        type: 'Manual Entry',
        moodBefore: newEntry.mood,
        moodAfter: newEntry.mood
      });
      setNewEntry({ reflection: '', mood: 3, tags: [] });
      setShowNewEntry(false);
    }
  };
  
  return (
    <div className="max-w-4xl mx-auto p-6">
      <button onClick={() => setCurrentView('home')} className="mb-6 text-slate-600 hover:text-slate-800 flex items-center gap-2">
        <Home size={20} /> Back to Home
      </button>
      
      <div className="flex justify-between items-center mb-8">
        <h2 className="text-4xl font-serif text-slate-800">My Journal</h2>
        <button
          onClick={() => setShowNewEntry(!showNewEntry)}
          className="px-6 py-3 bg-gradient-to-r from-green-500 to-teal-500 text-white rounded-xl hover:shadow-lg transition-all"
        >
          {showNewEntry ? 'Cancel' : '+ New Entry'}
        </button>
      </div>
      
      {showNewEntry && (
        <div className="bg-white rounded-3xl p-8 shadow-lg mb-8">
          <h3 className="text-2xl font-serif text-slate-800 mb-6">New Journal Entry</h3>
          
          <div className="space-y-6">
            <div>
              <label className="block text-slate-700 mb-2">How are you feeling?</label>
              <div className="flex gap-4 justify-center my-4">
                {MOODS.map(mood => (
                  <button
                    key={mood.label}
                    onClick={() => setNewEntry({...newEntry, mood: mood.value})}
                    className={`text-4xl p-3 rounded-2xl transition-all ${
                      newEntry.mood === mood.value ? 'bg-green-100 scale-125' : 'hover:scale-110'
                    }`}
                    title={mood.label}
                  >
                    {mood.emoji}
                  </button>
                ))}
              </div>
            </div>
            
            <div>
              <label className="block text-slate-700 mb-2">Your Reflection</label>
              <textarea
                value={newEntry.reflection}
                onChange={(e) => setNewEntry({...newEntry, reflection: e.target.value})}
                className="w-full p-4 rounded-xl border-2 border-slate-200 focus:border-green-400 focus:outline-none"
                rows="6"
                placeholder="What's on your mind today? What are you grateful for?"
              />
            </div>
            
            <button
              onClick={handleSaveEntry}
              className="w-full bg-gradient-to-r from-green-500 to-teal-500 text-white py-4 rounded-2xl text-lg font-semibold hover:shadow-xl transition-all"
            >
              Save Entry
            </button>
          </div>
        </div>
      )}
      
      <div className="space-y-4">
        {journals.length === 0 ? (
          <div className="text-center py-16">
            <div className="text-6xl mb-4">📖</div>
            <p className="text-xl text-slate-600">Your journal is empty</p>
            <p className="text-slate-500">Start writing to track your journey</p>
          </div>
        ) : (
          journals.slice().reverse().map((entry) => (
            <div key={entry.id} className="bg-white rounded-2xl p-6 shadow-md hover:shadow-lg transition-shadow">
              <div className="flex justify-between items-start mb-4">
                <div>
                  <div className="flex items-center gap-3 mb-2">
                    <span className="text-3xl">{MOODS.find(m => m.value === entry.moodAfter)?.emoji || '😌'}</span>
                    <div>
                      <h3 className="text-lg font-semibold text-slate-800">{entry.type}</h3>
                      <p className="text-sm text-slate-500">
                        {new Date(entry.date).toLocaleDateString('en-US', { 
                          weekday: 'long', 
                          year: 'numeric', 
                          month: 'long', 
                          day: 'numeric' 
                        })}
                      </p>
                    </div>
                  </div>
                </div>
                {entry.moodBefore !== undefined && entry.moodAfter !== undefined && (
                  <div className="text-right">
                    <p className="text-sm text-slate-600">Mood Shift</p>
                    <p className="text-lg font-semibold">
                      {MOODS.find(m => m.value === entry.moodBefore)?.emoji} → {MOODS.find(m => m.value === entry.moodAfter)?.emoji}
                    </p>
                  </div>
                )}
              </div>
              
              <p className="text-slate-700 leading-relaxed">{entry.reflection}</p>
              
              {entry.tags && entry.tags.length > 0 && (
                <div className="flex gap-2 mt-4">
                  {entry.tags.map((tag, idx) => (
                    <span key={idx} className="px-3 py-1 bg-purple-100 text-purple-700 rounded-full text-sm">
                      {tag}
                    </span>
                  ))}
                </div>
              )}
            </div>
          ))
        )}
      </div>
    </div>
  );
}

function ProgressView({ setCurrentView, sessions, journals }) {
  const getTotalMinutes = () => sessions.reduce((sum, s) => sum + s.duration, 0);
  
  const getStreak = () => {
    if (sessions.length === 0) return 0;
    let streak = 0;
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    
    for (let i = 0; i < 30; i++) {
      const checkDate = new Date(today);
      checkDate.setDate(checkDate.getDate() - i);
      const hasSession = sessions.some(s => {
        const sessionDate = new Date(s.date);
        sessionDate.setHours(0, 0, 0, 0);
        return sessionDate.getTime() === checkDate.getTime();
      });
      
      if (hasSession) {
        streak++;
      } else if (i > 0) {
        break;
      }
    }
    return streak;
  };
  
  const getMoodTrend = () => {
    return sessions.slice(-10).map((s, idx) => ({
      session: idx + 1,
      before: s.moodBefore,
      after: s.moodAfter
    }));
  };
  
  const getTypeDistribution = () => {
    const counts = {};
    sessions.forEach(s => {
      counts[s.type] = (counts[s.type] || 0) + 1;
    });
    return Object.entries(counts).map(([type, count]) => ({
      type: MEDITATION_TYPES.find(t => t.id === type)?.name || type,
      count
    }));
  };
  
  const getAverageMoodImprovement = () => {
    if (sessions.length === 0) return 0;
    const improvements = sessions.map(s => s.moodAfter - s.moodBefore);
    return (improvements.reduce((a, b) => a + b, 0) / improvements.length).toFixed(2);
  };
  
  const getMostEffectiveType = () => {
    const typeImprovements = {};
    sessions.forEach(s => {
      const improvement = s.moodAfter - s.moodBefore;
      if (!typeImprovements[s.type]) {
        typeImprovements[s.type] = { total: 0, count: 0 };
      }
      typeImprovements[s.type].total += improvement;
      typeImprovements[s.type].count += 1;
    });
    
    let bestType = null;
    let bestAvg = -Infinity;
    
    Object.entries(typeImprovements).forEach(([type, data]) => {
      const avg = data.total / data.count;
      if (avg > bestAvg) {
        bestAvg = avg;
        bestType = type;
      }
    });
    
    return MEDITATION_TYPES.find(t => t.id === bestType)?.name || bestType;
  };
  
  return (
    <div className="max-w-6xl mx-auto p-6">
      <button onClick={() => setCurrentView('home')} className="mb-6 text-slate-600 hover:text-slate-800 flex items-center gap-2">
        <Home size={20} /> Back to Home
      </button>
      
      <h2 className="text-4xl font-serif text-slate-800 mb-8">My Progress</h2>
      
      {sessions.length === 0 ? (
        <div className="text-center py-16">
          <div className="text-6xl mb-4">📊</div>
          <p className="text-xl text-slate-600">No data yet</p>
          <p className="text-slate-500">Complete your first meditation to see your progress</p>
        </div>
      ) : (
        <>
          <div className="grid md:grid-cols-4 gap-6 mb-8">
            <StatCard
              icon={<Clock className="text-blue-500" size={32} />}
              title="Total Minutes"
              value={getTotalMinutes()}
              suffix="min"
              color="bg-blue-50"
            />
            <StatCard
              icon={<Calendar className="text-green-500" size={32} />}
              title="Current Streak"
              value={getStreak()}
              suffix="days"
              color="bg-green-50"
            />
            <StatCard
              icon={<Award className="text-purple-500" size={32} />}
              title="Sessions"
              value={sessions.length}
              suffix=""
              color="bg-purple-50"
            />
            <StatCard
              icon={<TrendingUp className="text-pink-500" size={32} />}
              title="Avg Improvement"
              value={getAverageMoodImprovement()}
              suffix=""
              color="bg-pink-50"
            />
          </div>
          
          <div className="grid md:grid-cols-2 gap-6 mb-8">
            <div className="bg-white rounded-3xl p-6 shadow-lg">
              <h3 className="text-xl font-semibold text-slate-800 mb-6">Mood Transformation</h3>
              <ResponsiveContainer width="100%" height={300}>
                <LineChart data={getMoodTrend()}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="session" />
                  <YAxis domain={[0, 5]} />
                  <Tooltip />
                  <Legend />
                  <Line type="monotone" dataKey="before" stroke="#8b5cf6" name="Before" strokeWidth={2} />
                  <Line type="monotone" dataKey="after" stroke="#10b981" name="After" strokeWidth={2} />
                </LineChart>
              </ResponsiveContainer>
            </div>
            
            <div className="bg-white rounded-3xl p-6 shadow-lg">
              <h3 className="text-xl font-semibold text-slate-800 mb-6">Practice Types</h3>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={getTypeDistribution()}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="type" angle={-45} textAnchor="end" height={100} />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="count" fill="#8b5cf6" />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>
          
          <div className="bg-gradient-to-r from-purple-100 to-pink-100 rounded-3xl p-8">
            <h3 className="text-2xl font-serif text-slate-800 mb-4">Your Most Effective Practice</h3>
            <p className="text-lg text-slate-700">
              Based on your mood improvements, <strong>{getMostEffectiveType()}</strong> meditation 
              has been most beneficial for you. Keep practicing!
            </p>
          </div>
        </>
      )}
    </div>
  );
}

function StatCard({ icon, title, value, suffix, color }) {
  return (
    <div className={`${color} rounded-2xl p-6`}>
      <div className="mb-3">{icon}</div>
      <p className="text-slate-600 text-sm mb-1">{title}</p>
      <p className="text-3xl font-bold text-slate-800">
        {value}<span className="text-xl ml-1">{suffix}</span>
      </p>
    </div>
  );
}

function DiscoverView({ setCurrentView, bookmarkedContent, toggleBookmark }) {
  const [selectedContent, setSelectedContent] = useState(null);
  
  if (selectedContent) {
    return (
      <div className="max-w-4xl mx-auto p-6">
        <button 
          onClick={() => setSelectedContent(null)} 
          className="mb-6 text-slate-600 hover:text-slate-800 flex items-center gap-2"
        >
          ← Back to Discover
        </button>
        
        <div className="bg-white rounded-3xl p-8 shadow-xl">
          <div className="text-6xl mb-6 text-center">{selectedContent.icon}</div>
          <div className="mb-4 text-center">
            <span className="px-4 py-2 bg-purple-100 text-purple-700 rounded-full text-sm font-medium">
              {selectedContent.category}
            </span>
          </div>
          <h2 className="text-4xl font-serif text-slate-800 mb-6 text-center">{selectedContent.title}</h2>
          <div className="prose prose-lg max-w-none">
            <p className="text-slate-700 leading-relaxed whitespace-pre-line">
              {selectedContent.fullContent}
            </p>
          </div>
          <div className="mt-8 pt-6 border-t border-slate-200">
            <button
              onClick={() => toggleBookmark(selectedContent)}
              className={`w-full py-4 rounded-2xl font-semibold transition-all flex items-center justify-center gap-2 ${
                bookmarkedContent.some(b => b.title === selectedContent.title)
                  ? 'bg-pink-100 text-pink-700 hover:bg-pink-200'
                  : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
              }`}
            >
              <Star 
                size={20} 
                fill={bookmarkedContent.some(b => b.title === selectedContent.title) ? 'currentColor' : 'none'} 
              />
              {bookmarkedContent.some(b => b.title === selectedContent.title) ? 'Bookmarked' : 'Bookmark This'}
            </button>
          </div>
        </div>
      </div>
    );
  }
  
  return (
    <div className="max-w-6xl mx-auto p-6">
      <button onClick={() => setCurrentView('home')} className="mb-6 text-slate-600 hover:text-slate-800 flex items-center gap-2">
        <Home size={20} /> Back to Home
      </button>
      
      <h2 className="text-4xl font-serif text-slate-800 mb-8">Discover & Learn</h2>
      
      <div className="grid md:grid-cols-2 gap-6">
        {LEARN_CONTENT.map((content, idx) => {
          const isBookmarked = bookmarkedContent.some(b => b.title === content.title);
          return (
            <div key={idx} className="bg-white rounded-3xl p-8 shadow-lg hover:shadow-xl transition-shadow">
              <div className="flex justify-between items-start mb-4">
                <div className="text-5xl mb-4">{content.icon}</div>
                <button
                  onClick={() => toggleBookmark(content)}
                  className={`p-2 rounded-full transition-all ${
                    isBookmarked ? 'bg-pink-100 text-pink-600' : 'bg-slate-100 text-slate-400 hover:bg-pink-50'
                  }`}
                >
                  <Star size={20} fill={isBookmarked ? 'currentColor' : 'none'} />
                </button>
              </div>
              
              <div className="mb-2">
                <span className="px-3 py-1 bg-purple-100 text-purple-700 rounded-full text-sm font-medium">
                  {content.category}
                </span>
              </div>
              
              <h3 className="text-2xl font-serif text-slate-800 mb-3">{content.title}</h3>
              <p className="text-slate-600 leading-relaxed mb-4">{content.description}</p>
              
              <button 
                onClick={() => setSelectedContent(content)}
                className="mt-4 text-purple-600 hover:text-purple-700 font-semibold flex items-center gap-2"
              >
                Learn More →
              </button>
            </div>
          );
        })}
      </div>
      
      {bookmarkedContent.length > 0 && (
        <div className="mt-12">
          <h3 className="text-2xl font-serif text-slate-800 mb-6">Your Bookmarks</h3>
          <div className="grid md:grid-cols-3 gap-4">
            {bookmarkedContent.map((content, idx) => (
              <button
                key={idx}
                onClick={() => setSelectedContent(content)}
                className="bg-gradient-to-br from-pink-50 to-purple-50 rounded-2xl p-4 hover:shadow-lg transition-shadow text-left"
              >
                <div className="text-3xl mb-2">{content.icon}</div>
                <p className="font-semibold text-slate-800">{content.title}</p>
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}







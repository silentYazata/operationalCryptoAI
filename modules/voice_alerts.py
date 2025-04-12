from gtts import gTTS
import os
import platform

class VoiceAlerts:
    def __init__(self, language='en'):
        self.language = language

    def alert_trade_signal(self, signal):
        text = f"Trade signal: {signal}"
        self._speak(text)

    def alert_market_event(self, event):
        text = f"Market event: {event}"
        self._speak(text)

    def _speak(self, text):
        tts = gTTS(text=text, lang=self.language, slow=False)
        tts.save("alert.mp3")
        if platform.system() == "Darwin":  # macOS
            os.system("afplay alert.mp3")
        elif platform.system() == "Linux":  # Linux
            os.system("xdg-open alert.mp3")
        elif platform.system() == "Windows":  # Windows
            os.system("start alert.mp3")

# Example usage
if __name__ == "__main__":
    voice_alerts = VoiceAlerts()
    voice_alerts.alert_trade_signal("Buy Bitcoin")
    voice_alerts.alert_market_event("Ethereum price surge")
const sdk = require("microsoft-cognitiveservices-speech-sdk");

const speechConfig = sdk.SpeechConfig.fromSubscription(
  "<sua-chave>",
  "<região>"
);

speechConfig.speechSynthesisVoiceName = "pt-BR-AntonioNeural";

const synthesizer = new sdk.SpeechSynthesizer(speechConfig);

synthesizer.speakTextAsync(
  "Sua reserva foi confirmada para o dia 15 de julho.",
  result => {
    if (result) synthesizer.close();
  }
);

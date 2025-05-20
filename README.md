# Azure Cognitive Services: Language & Speech Studio

## 📌 Visão Geral
Exploração prática dos serviços de IA da Microsoft para processamento de linguagem natural e análise de sentimentos.

## 🔍 Recursos Principais

### 🗣️ Azure Speech Studio
| Funcionalidade | Descrição | Aplicações |
|--------------|----------|------------|
| Fala → Texto | Transcrição em tempo real | Call centers, legendas automáticas |
| Texto → Fala | Síntese de voz natural | Assistência virtual, acessibilidade |

### 📝 Azure Language Studio
| Funcionalidade | Exemplo | Saída |
|--------------|---------|-------|
| Análise de Sentimento | "Adorei o atendimento!" | Positivo (92%) |
| Extração de Palavras-Chave | "Quarto limpo e café da manhã excelente" | "quarto limpo", "café da manhã excelente" |
| Reconhecimento de Entidades | "Reserva para 2 pessoas em São Paulo" | "2" (número), "São Paulo" (local) |

## 🧪 Laboratório Prático

### 1. Configuração Inicial
```azurecli
az cognitiveservices account create \
  --name meu-servico-linguagem \
  --resource-group meu-rg \
  --kind TextAnalytics \
  --sku F0 \
  --location eastus

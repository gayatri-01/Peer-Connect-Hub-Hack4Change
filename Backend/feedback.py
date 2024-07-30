from nltk.sentiment import SentimentIntensityAnalyzer
from gensim.summarization import summarize
from textblob import TextBlob
from collections import Counter


def analyze_feedback(feedback):
    # Sentiment Analysis
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(feedback)

    # Topic Modeling
    summarized_feedback = summarize(feedback)

    # Named Entity Recognition
    feedback_blob = TextBlob(feedback)
    named_entities = feedback_blob.noun_phrases

    # Actionable Insights
    # Counting the most common noun phrases
    noun_phrase_counts = Counter(named_entities)
    top_noun_phrases = noun_phrase_counts.most_common(3)

    # Actionable Suggestions based on sentiment
    actionable_suggestions = []
    if sentiment_score["compound"] < -0.2:
        actionable_suggestions.append(
            "Address negative aspects mentioned in the feedback."
        )
    elif sentiment_score["compound"] > 0.2:
        actionable_suggestions.append(
            "Leverage positive aspects mentioned in the feedback."
        )

    return {
        "sentiment_score": sentiment_score,
        "summarized_feedback": summarized_feedback,
        "top_noun_phrases": top_noun_phrases,
        "actionable_suggestions": actionable_suggestions,
    }


# Example feedback text
feedback_text = """
I really enjoyed the service provided by your team. However, I think there is room for improvement in the delivery time. The product quality is excellent, but sometimes the packaging is not secure enough. Overall, I had a good experience but would appreciate faster delivery and better packaging.
"""

# Analyzing feedback
analysis_result = analyze_feedback(feedback_text)

# Printing the analysis result
print("Sentiment Score:", analysis_result["sentiment_score"])
print("Summarized Feedback:", analysis_result["summarized_feedback"])
print("Top Noun Phrases:", analysis_result["top_noun_phrases"])
print("Actionable Suggestions:", analysis_result["actionable_suggestions"])

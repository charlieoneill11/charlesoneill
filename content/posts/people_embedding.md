---
title: How to embed people
date: 2024-03-01
description: How can we turn people into vectors
---

# Vision

I started with the idea of a pendant that would glow green whenever you stood near someone who matched you on many dimensions. The glow would appear for both you and the other person, a way to tell you that you had found a kindred spirit. Obviously there was a flaw: no one wants to wear a pendant, no matter how magical. But the core insight remained. If we could embed a person in a multi-dimensional vector—incorporating their background, hobbies, professional track, and personality—we could compare that vector with others to find overlaps or interesting contrasts. 

Instead of a pendant, we can use an iPhone-based glow. When two users bring their phones close, the phone shows a score that measures their similarity (like the Airdrop or contact share feature). This single mechanic is free, fun, and easy to share on social media. The person who sees a high match score becomes curious. Where do they align with the other person? Which data in their combined embeddings triggered the high score?

This glow feature is only the entry point. Iris is a system that ingests data from Spotify, LinkedIn, Facebook, Netflix, or manual self-reports. It converts each data source into signals that feed a single representation of the user, a vector that evolves whenever the user adds or changes information. That same vector drives a search feature, where users can look for people with similar backgrounds or interests in a chosen location. It also powers a visual mode that shows a constellation of people in the user’s vicinity, with each point connected by degrees of similarity. There can be cool little features like finding your "lost twin": the person most similar to you in the world.

The consumer product is free. People use it because it reveals hidden commonalities and transforms everyday encounters into potential connections. Underneath, we gather the data that lets us do something more ambitious. Advertisers get a platform for precise targeting. Recruiters gain a way to pinpoint candidates with both the right skill set and the right personality. Recommendation engines can license these embeddings to improve how they tailor books, music, and products for each person.

We keep data usage transparent. Users toggle the sources they want to connect and can revoke them at any time. Our onboarding flow explains what data is shared and how it is folded into the embedding. This approach offers control. Users can remove or add feeds without friction, and their embeddings update accordingly.

We plan to enter the market by focusing on universities or events where people enjoy finding like-minded individuals. We expect early adopters to share videos of the glow score on TikTok, describing the surprise of discovering an exact match. That viral loop brings new signups, who then link their Spotify or LinkedIn, refining their own vector and making the system richer.

The idea works because the glow feature drives interest, and the embeddings deliver utility. As more people join, the embeddings become more accurate. (We will also have a strong technical moat in figuring out how to do structured embeddings properly.) Advertisers value the ability to place relevant content, recruiters see gains in sourcing, and consumer apps want to leverage the vectors for better recommendations. Iris becomes the global standard for representing people.

# Technical details

My goal was to iterate on this and get it deployed in a week. To do that, I saw three main steps to get the system up and running:
1. _Create synthetic training data for fine-tuning an encoder model._ To do this, I prompted `gpt-4o-mini` to generate
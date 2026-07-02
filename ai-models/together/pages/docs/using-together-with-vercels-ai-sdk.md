---
title: "Vercel AI SDK quickstart"
source: https://docs.together.ai/docs/using-together-with-vercels-ai-sdk
path: docs/using-together-with-vercels-ai-sdk
---

Use Together models with the Vercel AI SDK.

The Vercel AI SDK is a powerful Typescript library designed to help developers build AI-powered applications. Using Together AI and the Vercel AI SDK, you can easily integrate AI into your TypeScript, React, or Next.js project. In this tutorial, we'll look into how easy it is to use Together AI's models and the Vercel AI SDK.

## QuickStart: 15 lines of code

1. Install both the Vercel AI SDK and the Together AI provider package.

<CodeGroup>
  ```bash npm theme={null}
  npm i ai @ai-sdk/togetherai
  ```

  ```bash yarn theme={null}
  yarn add ai @ai-sdk/togetherai
  ```

  ```bash pnpm  theme={null}
  pnpm add ai @ai-sdk/togetherai
  ```
</CodeGroup>

2. Import the Together AI provider and call the `generateText` function with Kimi K2 to generate some text.

```js TypeScript theme={null}
import { generateText } from "ai";
import { createTogetherAI } from '@ai-sdk/togetherai';

const together = createTogetherAI({
  apiKey: process.env.TOGETHER_API_KEY ?? '',
});

async function main() {
  const { text } = await generateText({
    model: together("moonshotai/Kimi-K2.5"),
    prompt: "Write a vegetarian lasagna recipe for 4 people.",
  });

  console.log(text);
}

main();
```

### Output

```
Here's a delicious vegetarian lasagna recipe for 4 people:

**Ingredients:**

- 8-10 lasagna noodles
- 2 cups marinara sauce (homemade or store-bought)
- 1 cup ricotta cheese
- 1 cup shredded mozzarella cheese
- 1 cup grated Parmesan cheese
- 1 cup frozen spinach, thawed and drained
- 1 cup sliced mushrooms
- 1 cup sliced bell peppers
- 1 cup sliced zucchini
- 1 small onion, chopped
- 2 cloves garlic, minced
- 1 cup chopped fresh basil
- Salt and pepper to taste
- Olive oil for greasing the baking dish

**Instructions:**

1. **Preheat the oven:** Preheat the oven to 375°F (190°C).
2. **Prepare the vegetables:** Sauté the mushrooms, bell peppers, zucchini, and onion in a little olive oil until they're tender. Add the garlic and cook for another minute.
3. **Prepare the spinach:** Squeeze out as much water as possible from the thawed spinach. Mix it with the ricotta cheese and a pinch of salt and pepper.
4. **Assemble the lasagna:** Grease a 9x13-inch baking dish with olive oil. Spread a layer of marinara sauce on the bottom. Arrange 4 lasagna noodles on top.
5. **Layer 1:** Spread half of the spinach-ricotta mixture on top of the noodles. Add half of the sautéed vegetables and half of the shredded mozzarella cheese.
6. **Layer 2:** Repeat the layers: marinara sauce, noodles, spinach-ricotta mixture, sautéed vegetables, and mozzarella cheese.
7. **Top layer:** Spread the remaining marinara sauce on top of the noodles. Sprinkle with Parmesan cheese and a pinch of salt and pepper.
8. **Bake the lasagna:** Cover the baking dish with aluminum foil and bake for 30 minutes. Remove the foil and bake for another 10-15 minutes, or until the cheese is melted and bubbly.
9. **Let it rest:** Remove the lasagna from the oven and let it rest for 10-15 minutes before slicing and serving.

**Tips and Variations:**

- Use a variety of vegetables to suit your taste and dietary preferences.
- Add some chopped olives or artichoke hearts for extra flavor.
- Use a mixture of mozzarella and Parmesan cheese for a richer flavor.
- Serve with a side salad or garlic bread for a complete meal.

**Nutrition Information (approximate):**

Per serving (serves 4):

- Calories: 450
- Protein: 25g
- Fat: 20g
- Saturated fat: 8g
- Cholesterol: 30mg
- Carbohydrates: 40g
- Fiber: 5g
- Sugar: 10g
- Sodium: 400mg

Enjoy your delicious vegetarian lasagna!
```

## Streaming with the Vercel AI SDK

To stream from Together AI models using the Vercel AI SDK, simply use `streamText` as seen below.

```js TypeScript theme={null}
import { streamText } from "ai";
import { createTogetherAI } from '@ai-sdk/togetherai';

const together = createTogetherAI({
  apiKey: process.env.TOGETHER_API_KEY ?? '',
});

async function main() {
  const result = await streamText({
    model: together("moonshotai/Kimi-K2.5"),
    prompt: "Invent a new holiday and describe its traditions.",
  });

  for await (const textPart of result.textStream) {
    process.stdout.write(textPart);
  }
}

main();
```

### Output

```
Introducing "Luminaria Day" - a joyous holiday celebrated on the spring equinox, marking the return of warmth and light to the world. This festive occasion is a time for family, friends, and community to come together, share stories, and bask in the radiance of the season.

**Date:** Luminaria Day is observed on the spring equinox, typically around March 20th or 21st.

**Traditions:**

1. **The Lighting of the Lanterns:** As the sun rises on Luminaria Day, people gather in their neighborhoods, parks, and public spaces to light lanterns made of paper, wood, or other sustainable materials. These lanterns are adorned with intricate designs, symbols, and messages of hope and renewal.
2. **The Storytelling Circle:** Families and friends gather around a central fire or candlelight to share stories of resilience, courage, and triumph. These tales are passed down through generations, serving as a reminder of the power of human connection and the importance of learning from the past.
3. **The Luminaria Procession:** As the sun sets, communities come together for a vibrant procession, carrying their lanterns and sharing music, dance, and laughter. The procession winds its way through the streets, symbolizing the return of light and life to the world.
4. **The Feast of Renewal:** After the procession, people gather for a festive meal, featuring dishes made with seasonal ingredients and traditional recipes. The feast is a time for gratitude, reflection, and celebration of the cycle of life.
5. **The Gift of Kindness:** On Luminaria Day, people are encouraged to perform acts of kindness and generosity for others. This can take the form of volunteering, donating to charity, or simply offering a helping hand to a neighbor in need.

**Symbolism:**

* The lanterns represent the light of hope and guidance, illuminating the path forward.
* The storytelling circle symbolizes the power of shared experiences and the importance of learning from one another.
* The procession represents the return of life and energy to the world, as the seasons shift from winter to spring.
* The feast of renewal celebrates the cycle of life, death, and rebirth.
* The gift of kindness embodies the spirit of generosity and compassion that defines Luminaria Day.

**Activities:**

* Create your own lanterns using recycled materials and decorate them with symbols, messages, or stories.
* Share your own stories of resilience and triumph with family and friends.
* Participate in the Luminaria Procession and enjoy the music, dance, and laughter.
* Prepare traditional dishes for the Feast of Renewal and share them with loved ones.
* Perform acts of kindness and generosity for others, spreading joy and positivity throughout your community.

Luminaria Day is a time to come together, celebrate the return of light and life, and honor the power of human connection.
```

## Image Generation

To generate images with Together AI models using the Vercel AI SDK, use the `.image()` factory method. For more on image generation with the AI SDK see [generateImage()](https://ai-sdk.dev/docs/reference/ai-sdk-core/generate-image).

```js TypeScript theme={null}
import { createTogetherAI } from '@ai-sdk/togetherai';
import { generateImage } from 'ai';

const togetherai = createTogetherAI({
  apiKey: process.env.TOGETHER_API_KEY ?? '',
});

const { images } = await generateImage({
  model: togetherai.image('black-forest-labs/FLUX.1-schnell'),
  prompt: 'A delighted resplendent quetzal mid flight amidst raindrops',
});

// The images array contains base64-encoded image data by default
```

You can pass optional provider-specific request parameters using the `providerOptions` argument.

```js TypeScript theme={null}
import { createTogetherAI } from '@ai-sdk/togetherai';
import { generateImage } from 'ai';

const togetherai = createTogetherAI({
  apiKey: process.env.TOGETHER_API_KEY ?? '',
});

const { images } = await generateImage({
  model: togetherai.image('black-forest-labs/FLUX.1-schnell'),
  prompt: 'A delighted resplendent quetzal mid flight amidst raindrops',
  size: '512x512',
  // Optional additional provider-specific request parameters
  providerOptions: {
    togetherai: {
      steps: 40,
    },
  },
});
```

Together AI image models support various image dimensions that vary by model. Common sizes include 512x512, 768x768, and 1024x1024, with some models supporting up to 1792x1792. The default size is 1024x1024.

Available Models:

* `black-forest-labs/FLUX.1-schnell`
* `black-forest-labs/FLUX.1.1-pro`
* `black-forest-labs/FLUX.1-kontext-pro`
* `black-forest-labs/FLUX.1-kontext-max`
* `black-forest-labs/FLUX.1-krea-dev`

Please see the [Together AI models page](https://docs.together.ai/docs/serverless/models#image-models) for a full list of available image models and their capabilities.

## Embedding Models

To embed text with Together AI models using the Vercel AI SDK, use the `.embeddingModel()` factory method.
For more on embedding models with the AI SDK see [embed()](https://ai-sdk.dev/docs/reference/ai-sdk-core/embed).

```js TypeScript theme={null}
import { createTogetherAI } from '@ai-sdk/togetherai';
import { embed } from 'ai';

const togetherai = createTogetherAI({
  apiKey: process.env.TOGETHER_API_KEY ?? '',
});

const { embedding } = await embed({
  model: togetherai.embeddingModel('intfloat/multilingual-e5-large-instruct'),
  value: 'sunny day at the beach',
});
```

<Note>
  For a complete list of available embedding models and their model IDs, see the [Together AI models
  page](https://docs.together.ai/docs/serverless/models#embedding-models).
</Note>

Some available model IDs include:

* `intfloat/multilingual-e5-large-instruct`

***

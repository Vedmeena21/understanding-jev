// Jev quickstart (TypeScript)
//
// npm install @typesafe-ai/sdk
// export TYPESAFE_API_KEY="your-key"
// npx tsx quickstart.ts

import { choice, TypeSafeClient } from "@typesafe-ai/sdk";

const client = new TypeSafeClient(); // reads TYPESAFE_API_KEY

const response = await client.systemOne({
  state: { document: "I was charged twice. Please fix this ASAP." },
  questions: {
    category: choice("What is this ticket about?", {
      billing: null,
      technical: null,
      other: null,
    }),
  },
});

console.log(response.answers.category.choice); // "billing"

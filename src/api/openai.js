import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: process.env.REACT_APP_OPENAI_API_KEY, 
    dangerouslyAllowBrowser: true
  });

export const get_chat_completion = async (input) => {
    const response = await openai.chat.completions.create({
        model: "gpt-4o-mini",
        temperature: 0,
        messages: input
    });

    return (response.choices[0].message.content)
}

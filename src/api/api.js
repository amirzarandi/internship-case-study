export const getAIMessage = async (input, history) => {
  try {
    const encodedInput = encodeURIComponent(input);
    const encodedHistory = encodeURIComponent(JSON.stringify(history));
    const url = `http://127.0.0.1:5000/ask_chat_langchain?input=${encodedInput}&history=${encodedHistory}`;

    const response = await fetch(url, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();

    return data.response;
  } catch (error) {
    console.error('Error fetching AI message:', error);
    return null;
  }
};


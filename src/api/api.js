import { ask_chat } from "./integration";

const BaoDistributors = '63fef3606c20c1f22a700db3' // Trained on home_depot_data_2021.csv

const chatID = BaoDistributors
const history = []

export const getAIMessage = async (input) => {

  const response = await ask_chat(input, history)
  history.push({role: "user", content: input})
  history.push({role: "assistant", content: response})

  return response;
};

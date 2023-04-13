import { createStore, combineReducers } from "redux";
import { machinesReduser } from "./machinesReduser";
import { composeWithDevTools } from "redux-devtools-extension"

const rootReduser = combineReducers({
    machines: machinesReduser,
})


export const store = createStore(rootReduser, composeWithDevTools())
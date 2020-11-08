import { connectRouter, routerMiddleware } from "connected-react-router";
import { createBrowserHistory } from "history";
import { applyMiddleware, combineReducers, createStore } from "redux";
import thunk from "redux-thunk";

export const history = createBrowserHistory();
const middlewares = [thunk, routerMiddleware(history)];
const rootReducer = combineReducers({ router: connectRouter(history) });

export const store = createStore(rootReducer, applyMiddleware(...middlewares));

export type RootState = ReturnType<typeof rootReducer>;

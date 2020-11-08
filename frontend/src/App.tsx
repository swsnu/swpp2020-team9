import React, { ReactElement } from "react";
import { History } from "history";
import { ConnectedRouter } from "connected-react-router";
import { Redirect, Route, Switch } from "react-router";

import "./App.css";

import Navbar from "./containers/navbar/Navbar";
import Signin from "./containers/user/Signin";
import Signup from "./containers/user/Signup";
import Explore from "./containers/plan/Explore";
import View from "./containers/plan/View";
import Create from "./containers/plan/Create";
import ErrorPage from "./containers/system/ErrorPage";

interface Props {
  history: History;
}

function App(props: Props): ReactElement {
  const { history } = props;

  return (
    <ConnectedRouter history={history}>
      <div className="App">
        <Navbar />
        <Switch>
          <Route path="/signin" exact component={Signin} />
          <Route path="/signup" exact component={Signup} />
          <Route path="/plan/explore" exact component={Explore} />
          <Route path="/plan/view" exact component={View} />
          <Route path="/plan/create" exact component={Create} />
          <Redirect from="/" exact to="/signin" />
          <Route component={ErrorPage} />
        </Switch>
      </div>
    </ConnectedRouter>
  );
}

export default App;

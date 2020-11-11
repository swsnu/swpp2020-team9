import React, { ReactElement } from "react";
import { History } from "history";
import { ConnectedRouter } from "connected-react-router";
import { Redirect, Route, Switch } from "react-router";

import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

import Navbar from "./components/NB";
import Signin from "./containers/user/Signin";
import Signup from "./containers/user/Signup";
import Home from "./containers/home/Home";
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
        <Navbar history={history} username="username123" />
        <Switch>
          <Route path="/signin" exact component={Signin} />
          <Route path="/signup" exact component={Signup} />
          <Route path="/home" exact component={Home} />
          <Route
            path="/plan/explore"
            exact
            render={() => <Explore history={history} />}
          />
          <Route path="/plan/view/:id" exact component={View} />
          <Route path="/plan/create" exact component={Create} />
          <Redirect from="/" exact to="/signin" />
          <Route component={ErrorPage} />
        </Switch>
      </div>
    </ConnectedRouter>
  );
}

export default App;

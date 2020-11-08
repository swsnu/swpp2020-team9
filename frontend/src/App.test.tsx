import React, { ReactElement } from "react";
import { Provider } from "react-redux";
import { mount } from "enzyme";

import { store, history } from "./configure";
import App from "./App";

describe("<App />", () => {
  let appComponent: ReactElement;
  beforeEach(() => {
    appComponent = (
      <Provider store={store}>
        <App history={history} />
      </Provider>
    );
  });

  it("should render without errors", () => {
    const component = mount(appComponent);
    const wrapper = component.find(".App");
    expect(wrapper.length).toBe(1);
  });
});

import React, { ReactElement } from "react";
import { History } from "history";
import PlanCardDeck from "../../components/card/PlanCardDeck";

interface Props {
  history: History;
}

function Explore(props: Props): ReactElement {
  const { history } = props;

  return (
    <div className="Explore">
      <PlanCardDeck history={history} />
    </div>
  );
}

export default Explore;

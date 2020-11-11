import React, { ReactElement } from "react";
import { History } from "history";
import Card from "react-bootstrap/Card";

export interface CardProps {
  image: string;
  title: string;
  text: string;
  author: string;
}

interface Props extends CardProps {
  history: History;
}

function PlanCard(props: Props): ReactElement {
  const { image, title, text, author, history } = props;

  return (
    <Card onClick={() => history.push("/plan/view/1")}>
      <Card.Header>{title}</Card.Header>
      <Card.Img bsPrefix="card-img CardBackgroundImage" src={image} />
      <Card.Footer>
        <small className="text-muted">by {author}, updated 3 mins ago</small>
      </Card.Footer>
    </Card>
  );
}

export default PlanCard;

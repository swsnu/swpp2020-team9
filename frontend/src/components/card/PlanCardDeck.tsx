import React, { ReactElement } from "react";
import { History } from "history";
import CardDeck from "react-bootstrap/CardDeck";
import PlanCard, { CardProps } from "./Card";
import Image1 from "./trip_placeholder_1.jpg";
import Image2 from "./trip_placeholder_2.jpg";
import Image3 from "./trip_placeholder_3.jpg";
import Image4 from "./trip_placeholder_4.jpg";
import Image5 from "./trip_placeholder_5.jpg";

interface Props {
  history: History;
}

function PlanCardDeck(props: Props): ReactElement {
  const { history } = props;
  const cardProps: CardProps[] = [
    {
      image: Image1,
      title: "My Plan for Awesome Trip!",
      text: "while True:\nself.eat()",
      author: "Jeong-ho",
    },
    {
      image: Image2,
      title: "My Plan for Awesome Trip!",
      text: "while True:\nself.drink()",
      author: "Geon-woo",
    },
    {
      image: Image4,
      title: "My Plan for Awesome Trip!",
      text: "while True:\nself.dance()",
      author: "Jae-joon",
    },
    {
      image: Image5,
      title: "My Plan for Awesome Trip!",
      text: "while True:\nself.sing()",
      author: "Author123",
    },
  ];

  const cards = cardProps.map((cardProp) => {
    const { image, title, text, author } = cardProp;

    return (
      <PlanCard
        image={image}
        title={title}
        text={text}
        author={author}
        history={history}
      />
    );
  });

  return <CardDeck>{cards}</CardDeck>;
}

export default PlanCardDeck;

import React, { ReactElement } from "react";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import NavDropdown from "react-bootstrap/NavDropdown";
import { History } from "history";

interface Props {
  history: History;
  username: string;
}

function NB(props: Props): ReactElement {
  const { history, username } = props;

  return (
    <Navbar bg="light" expand="lg">
      <Navbar.Brand onClick={() => history.push("/home")}>PLAND</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <Nav.Link onClick={() => history.push("/home")}>Home</Nav.Link>
          <Nav.Link onClick={() => history.push("/plan/explore")}>
            Explore
          </Nav.Link>
        </Nav>
        <Nav className="mr-sm-2">
          <NavDropdown title={username} id="basic-nav-dropdown">
            <NavDropdown.Item onClick={() => history.push("/user/profile")}>
              Profile
            </NavDropdown.Item>
            <NavDropdown.Item onClick={() => history.push("/user/plans")}>
              Plans
            </NavDropdown.Item>
            <NavDropdown.Item onClick={() => history.push("/user/pins")}>
              Pins
            </NavDropdown.Item>
            <NavDropdown.Divider />
            <NavDropdown.Item href="#action/3.4">Sign Out</NavDropdown.Item>
          </NavDropdown>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
}

export default NB;

import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';

const NavBar = () => {
  return (
    <nav>
      <div>banner</div>
      <NavLink to="/" exact={true} activeClassName="active">
        Home
      </NavLink>
      <NavLink to="/login" exact={true} activeClassName="active">
        Login
      </NavLink>
      <NavLink to="/sign-up" exact={true} activeClassName="active">
        Sign Up
      </NavLink>
      <LogoutButton />
    </nav>
  );
}

export default NavBar;

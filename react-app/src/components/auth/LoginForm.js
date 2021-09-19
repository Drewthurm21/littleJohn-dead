import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { login } from '../../store/session'
import './Forms.css'

const LoginForm = () => {
  const dispatch = useDispatch();
  const user = useSelector(state => state.session.user);
  const welcomeLogo = require('../../images/welcomeLogo.png')

  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const onLogin = async (e) => {
    console.log('we ouyt here')
    e.preventDefault();
    const data = dispatch(login(email, password));
    if (data.errors) setErrors(data.errors);
  };

  const demoLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login('demo@aa.io', 'password'));
    if (data.errors) setErrors(data.errors);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <div className='login-page-wrapper'>
      <div className='splash-image-container'></div>
      <div className='form-side'>
        <div className='welcome-logo-container'>
          <img src={welcomeLogo} alt='welcome-logo' className='welcome-logo'></img>
        </div>
        <div className='login-form-container'>
          <form className="login-form">
            <div className='form-errors'>
              {errors.map((error) => (
                <div>{error}</div>
              ))}
            </div>
            <div>
              <input
                required={true}
                name="email"
                type="text"
                value={email}
                onChange={updateEmail}
              />
              <label htmlFor="email">Email</label>
            </div>
            <div>
              <input
                required={true}
                name="password"
                type="password"
                value={password}
                onChange={updatePassword}
              />
              <label htmlFor="password">Password</label>
            </div>
            <div className='login-buttons'>
              <button type="submit" onClick={onLogin}>Login</button>
              <button type="submit" onClick={demoLogin}>Demo Login</button>
            </div>
          </form>
          <div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LoginForm;

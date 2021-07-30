import React, { useState } from "react";
import { useDispatch } from "react-redux";


const TestForm = () => {
  const dispatch = useDispatch();
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [date, setDate] = useState('')
  const [message, setMessage] = useState('')


  const submitForm = async () => {
    const newRow = JSON.stringify({
      name: name,
      email: email,
      date: date,
      message: message
    })

    const res = await fetch('https://sheet.best/api/sheets/476ad59e-9cbe-47d9-93e4-44df9123c7a4',
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: newRow
      })
  }

  return (
    <form>
      <div>
        <label for="name">Name</label>
        <input
          name="name"
          type="text"
          placeholder="name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </div>
      <div>
        <label for="email">Email</label>
        <input
          name="email"
          type="text"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>
      <div>
        <label for="date">Date</label>
        <input
          name="date"
          type="text"
          placeholder="date"
          value={date}
          onChange={(e) => setDate(e.target.value)}
        />
      </div>
      <div>
        <label for="message">Message</label>
        <input
          name="message"
          type="text"
          placeholder="message"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
      </div>
      <br></br>
      <br></br>
      <br></br>
      <div onClick={submitForm}>Send</div>

    </form>
  );
};

export default TestForm;

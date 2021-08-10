import React, { useState } from "react";

const TestForm = () => {
  const [postId, setPostId] = useState(0)
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [date, setDate] = useState('')
  const [message, setMessage] = useState('')
  const [price, setPrice] = useState(0)

  const initials = ['DT', 'SS', 'MC']
  const initialsOptions = initials.map(init => (
    <option>{init}</option>
  ))
  const employees = ['Drew Thurman', 'Scott Schrader', 'Mike Christ']

  const submitForm = async () => {
    setPostId(postId + 1)

    console.log(postId)

    const newRow = JSON.stringify({
      id: postId + 1,
      name: name,
      email: email,
      date: date,
      message: message,
      price: price
    })

    console.log(newRow)

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
        <label for="initials">Initials</label>
        <select>
          {initialsOptions}
        </select>
      </div>
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
          type="date"
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
      <div>
        <label for="price">Price</label>
        <input
          name="price"
          type="text"
          placeholder="price"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
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

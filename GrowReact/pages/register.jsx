import Head from 'next/head';
import { useState } from 'react';

function Register({ message }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  async function handleSubmit(e) {
    e.preventDefault();

    try {
      const res = await fetch('/register_user', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
      });

      if (!res.ok) {
        throw new Error(await res.text());
      }

      window.location.href = '/login';
    } catch (error) {
      setMessage(error.message);
    }
  }

  return (
    <>
      <Head>
        <title>注册</title>
      </Head>

      <div className="container mt-5">
        {message && (
          <div className="alert alert-danger" role="alert">
            {message}
          </div>
        )}

        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label htmlFor="username" className="form-label">
              用户名
            </label>
            <input
              type="text"
              className="form-control"
              id="username"
              name="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>

          <div className="mb-3">
            <label htmlFor="password" className="form-label">
              密码
            </label>
            <input
              type="password"
              className="form-control"
              id="password"
              name="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>

          <div className="d-grid gap-2">
            <button className="btn btn-primary" type="submit">
              注册
            </button>
          </div>
        </form>
      </div>
    </>
  );
}

export default Register;
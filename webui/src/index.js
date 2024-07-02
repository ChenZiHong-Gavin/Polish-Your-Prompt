import React from 'react';
import ReactDOM from 'react-dom/client';
import { RouterProvider } from 'react-router';
import "./index.css"
import routes from './router';

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <RouterProvider router={routes} />
);

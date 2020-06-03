import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import * as serviceWorker from './serviceWorker';
import Grid from '@material-ui/core/Grid';
import App from './App';
import Imageupload from './components/Imageupload';
import  Social  from './components/Social';
import Result from './components/Result';
import About from './components/About'
import { Container, Header, Content, Footer, } from 'rsuite';
import Paper from '@material-ui/core/Paper';
ReactDOM.render(
  <div>
  <Container>
      <Header><App /></Header>
      <Container>
     <Grid container spacing={24}>
          <Grid item xs={6}>
          <Paper> <Result /></Paper>
          </Grid>
          <Grid item xs={6}>
            <Paper > <Imageupload /></Paper>
          </Grid>
        </Grid>
      </Container>
      
      <Footer><Social /></Footer>
      </Container>

  </div>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();

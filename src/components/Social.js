import React,{Component} from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {  faGithub  } from '@fortawesome/fontawesome-free-brands';
import { faEnvelope,faHome,} from '@fortawesome/free-solid-svg-icons';

//Footer section that contains icons that link to social media for representing contact details

class  Social extends Component{
  render(){
          return(
  <div className="footer">
    <a  href="https://2020batch23.blogspot.com/" className={'button'}
     title="Blogger">
      <FontAwesomeIcon icon={faHome} size='3x' color='black' />
    </a>
    <a
      href='https://github.com/Shreyas2409/Pneumonia-Prediction-using-Medical-Image-Modality'
      title='Github repo'
      className={'button'}
    >
      <FontAwesomeIcon icon={faGithub} size='3x' color='black' />
    </a>
    <a
     href='www.gmail.com'
      title='batch23dp@gmail.com'
      className={'button'}
    >
      <FontAwesomeIcon icon={faEnvelope} size='3x' color='black' />
    </a>
  </div>
          );
  }
}
export default Social;

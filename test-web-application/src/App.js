import './App.css';
import axios from 'axios';
import Cookies from 'js-cookie'

function App() {

  function auth() {
    let params = window.location.toString().split('/');
    const url = `https://${params[2]}/testing/auth?key=${params[params.length - 1]}`;
    window.location = url;
  }

  function getUserInfo() {
    let csrf_token = Cookies.get('csrf-token');
    let params = window.location.toString().split('/');

    axios.get(`https://${params[2]}/testing/userinfo`,
      {
        withCredentials: true,
        headers: { 'X-Token': csrf_token }
      }

    )
      .then((resp) => document.getElementById('msg').innerText = "Hello " + resp.data.name + ",");
  }




  return (
    <div className="App">
      <header className="App-header">
        <h4>App 1 - Webhosting</h4>
        <img src="https://react.yorickcleerbout.be/static/media/cookie.png" className="App-logo" alt="logo" />
        <h3 id="msg"></h3>

        <div class="btn-group">
          <button id="auth" onClick={auth}>Authorize with External IDP</button>
          <button id="info" onClick={getUserInfo}>Get User Info</button>
        </div>


      </header>
    </div>
  );
}



export default App;

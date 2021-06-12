import { getData, postData } from './services/APILayer';
import { useState } from 'react';
import { TextField, Button } from '@material-ui/core';
import './App.css';

function App() {

  const [search, setSearch] = useState('');
  const [teamData, setTeamData] = useState({
    team_name: '',
    team_role: ''
  });
  const [queryResult, setQueryResult] = useState([])
  const [status, setStatus] = useState('')

  const updateValue = (event, param) => {
    setTeamData({ ...teamData, [param]: event.target.value})
  }
  const updateSearch = event => {
    setSearch(event.target.value)
  }
  const addTeam = async (event) => {
    if (teamData.team_name === '') {
      alert('Team name cannot be empty')
    }
    else if (teamData.team_role === '') {
      alert('Team name cannot be empty')
    } else {
      const status = await postData(teamData)
      setStatus(status)
    }
  }
  const getTeam = async () => {
    const res = await getData(search);
    setQueryResult(res);
  }

  return (
    <div className="App">
      <h1>Cargill teams app</h1>
      <div className="content">
        <div className="add-team">
          <h2>Add team data</h2>
          <div className="container">
            <TextField
              className="team-name"
              label="Enter team name"
              size="small"
              variant="outlined"
              onChange={event => updateValue(event, 'team_name')} />
            <TextField
              label="Enter role"
              size="small"
              variant="outlined"
              onChange={event => updateValue(event, 'team_role')} />
          </div>
          <div className="btn-group">
          <Button className="btn-submit" variant="contained" color="primary" onClick={addTeam}>Submit</Button>
          </div>
          <div className={`message ${(status.message || '').includes('Error') ? 'error' : 'success'}`}>
            {status.message}
          </div>
        </div>
        <div className="query-team">
          <h2>Query team data</h2>
          <div className="container">
            <TextField
              label="Search team name"
              size="small"
              variant="outlined"
              onChange={updateSearch} />
          </div>
          <Button variant="contained" color="primary" onClick={getTeam}>Query</Button>
          <h3 style={{ textAlign: "left" }}>Result (Roles):</h3>
          <div className="result">
            <ul>
              {queryResult.map(row => {
                return (
                  <li className={`list ${(row || '').includes('Error') ? 'error' : 'success'}`}>
                    {row}
                  </li>
                )
              })}
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

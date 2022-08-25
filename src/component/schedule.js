import {Container, Table} from "react-bootstrap";
const Schedule = () => {
  return(
      <Container >
        <br/>
        <Table striped bordered hover>
          <thead>
              <tr>
                <th>User Name</th>
                <th>Warehouse Name</th>
                <th>Date</th>
                <th>shift</th>
                <th>City</th>
              </tr>
          </thead>
          <tbody>
            <tr>
                <td>User Name</td>
                <td>Warehouse Name</td>
                <td>Date</td>
                <td>shift</td>
                <td>City</td>
            </tr>
          </tbody>
        </Table>
      </Container>);
}
export default Schedule;
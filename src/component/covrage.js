import React, {useState} from "react";
import {Container, Table, DropdownButton , Dropdown ,Button} from "react-bootstrap";
import axios from "axios";

const Coverage = () => {
    const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    const mouth = new Date().getMonth()
    const [coverage,setCoverage] = useState([]);
    const [month,setMonth] = useState(months[mouth]);
    async function getCoverage(month){
        let coverage
        await axios.post('http://127.0.0.1:8000/test/emp',{
                month:month
            }
        ).then(res => {
            coverage = Object.values(res.data)
        })
        setCoverage(coverage)
    }

    return(
        <Container >
            <br/>
            <DropdownButton id="dropdown-basic-button" title={month}>
                {months.map( (value) =>
                    <Dropdown.Item onClick={() => getCoverage(value)}>{value}</Dropdown.Item>
                )}
            </DropdownButton>

            <br/>
            <Table striped bordered hover>
                <thead>
                <tr>
                    <th>User Name</th>
                    <th>Warehouse Name</th>
                    <th>Date</th>
                    <th>shift</th>
                </tr>
                </thead>
                <tbody>
                {coverage.map(value => {
                    return(
                        <tr>
                            <td>{value["warehouse"]}</td>
                            <td>{value["name"]}</td>
                            <td>{value["month"]+" "+value["day"]}</td>
                            <td>{value["shift"]}</td>
                        </tr>
                    )
                })}
                </tbody>
            </Table>
        </Container>
    );
};
export default Coverage;
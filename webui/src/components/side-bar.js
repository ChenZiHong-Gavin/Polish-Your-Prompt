import {Menu} from "react-daisyui"


const SideBar = ({ children }) => {
    return (
        <>
            <Menu>
                <Menu.Item>
                    <button>Item 1</button>
                </Menu.Item>
            </Menu>
        </>
    );
}

export default SideBar;

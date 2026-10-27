import sqlite3
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Employee Directory")

DATABASE_PATH = r"C:\Users\DELL\OneDrive\Documents\thesis\employee_directory.db"


@mcp.tool()
def search_employee(name: str) -> str:
    """
    Search the employee directory by employee name.
    """

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT Employee_ID,
               Employee_Name,
               Department,
               Position,
               Country
        FROM employees
        WHERE Employee_Name LIKE ?
        LIMIT 10
        """,
        (f"%{name}%",)
    )

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return "No employee found."

    results = []

    for row in rows:
        results.append(
            f"""
Employee ID: {row[0]}
Name: {row[1]}
Department: {row[2]}
Position: {row[3]}
Country: {row[4]}
"""
        )

    return "\n".join(results)


@mcp.tool()
def find_employees_by_department(department: str) -> str:
    """
    Find employees belonging to a specific department.
    """

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT Employee_ID,
               Employee_Name,
               Position,
               Country
        FROM employees
        WHERE Department LIKE ?
        LIMIT 20
        """,
        (f"%{department}%",)
    )

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return "No employees found in that department."

    results = []

    for row in rows:
        results.append(
            f"""
Employee ID: {row[0]}
Name: {row[1]}
Position: {row[2]}
Country: {row[3]}
"""
        )

    return "\n".join(results)


@mcp.tool()
def get_employee_profile(employee_id: str) -> str:
    """
    Get information about a specific employee using employee ID.
    """

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM employees
        WHERE Employee_ID = ?
        LIMIT 1
        """,
        (employee_id,)
    )

    row = cursor.fetchone()

    column_names = [
        description[0]
        for description in cursor.description
    ] if cursor.description else []

    conn.close()

    if not row:
        return "Employee not found."

    profile = dict(zip(column_names, row))

    return "\n".join(
        f"{key}: {value}"
        for key, value in profile.items()
    )


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http"
    )
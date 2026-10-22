from sqlalchemy.orm import Session
from models.database import get_db
from models.ticketModel import Ticket
from models.ticketSchema import TicketCreate, TicketResponse
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


# Create a ticket
# Status code 201 means Created
@router.post("/ticket", response_model=TicketResponse, status_code=201)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    new_ticket = Ticket(
        title=ticket.title, status=ticket.status, description=ticket.description
    )
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket


# Get all tickets
@router.get("/tickets", response_model=list[TicketResponse])
def get_all_tickets(db: Session = Depends(get_db)):
    tickets = db.query(Ticket).all()
    return tickets


@router.get("/ticket/{status}", response_model=list[TicketResponse])
def ger_ticket(status: str, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.status == status).all()
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found, try again")
    return ticket


@router.put("/ticket/{ticket_id}", response_model=TicketResponse)
def update_ticket(ticket_id: int, ticket: TicketCreate, db: Session = Depends(get_db)):
    ticket1 = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found, try again")
    ticket1.title = ticket.title
    ticket1.status = ticket.status
    ticket1.description = ticket.description
    db.commit()
    db.refresh(ticket1)
    return ticket1


@router.delete("/ticket/{ticket_id}")
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found, try again")
    db.delete(ticket)
    db.commit()
    return {"message": "Item deleted successfully", "id": ticket_id}

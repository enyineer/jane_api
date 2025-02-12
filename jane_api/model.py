from typing import Any, List, Optional, Dict
from pydantic import BaseModel, Field, HttpUrl

class Avatar(BaseModel):
    id: str
    path: HttpUrl
    source: str

class Light(BaseModel):
    wattage: str
    type: str

class Timestamp(BaseModel):
    _seconds: int
    _nanoseconds: int

class ChangedEnvironment(BaseModel):
    exposureTime: int
    name: str
    type: str
    lights: List[Light]

class EnvironmentChange(BaseModel):
    date: str
    environment: ChangedEnvironment
    original_environment: Optional[ChangedEnvironment] = None
    changes: List[str]
    _type: str
    active: bool

class Environment(BaseModel):
    type: str
    lights: List[Light]
    name: str
    exposureTime: int
    avatar: Optional[Avatar] = None
    indoorLength: Optional[int] = None
    indoorWidth: Optional[int] = None
    environment_changes: List[EnvironmentChange]
    indoorHeight: Optional[int] = None
    updatedAt: Optional[Timestamp] = None

class Log(BaseModel):
    date: str
    timestamp: Optional[Timestamp] = None

class RRule(BaseModel):
    weeklyDays: List[str]
    period: Optional[int] = None
    limitTimes: Optional[int] = None
    limitStage: Optional[str] = None
    limitDate: Optional[str] = None
    limitType: Optional[str] = None
    frequency: Optional[str] = None

class Amount(BaseModel):
    unit: str
    value: str

class Nutrient(BaseModel):
    producerName: Optional[str] = None
    description: Optional[str] = None
    name: str
    logo: Any
    id: Optional[str] = None
    producerId: Optional[str] = None

class Mix(BaseModel):
    amount: Optional[Amount] = None
    nutrient: Optional[Nutrient] = None
    solvent: Optional[Amount] = None

class ReminderEvent(BaseModel):
    date: str
    application_method: Optional[str] = None
    environments: List[str]
    _type: str
    active: bool
    environmentsTrees: Dict[str, List[str]]
    exclusions: List[str]
    type: str
    isDone: Optional[bool] = None
    rrule: Optional[RRule] = None
    mixes: Optional[List[Mix]] = None
    description: Optional[str] = None
    logs: Dict[str, Log]
    timestamp: Optional[Timestamp] = None
    updatedAt: Optional[Timestamp] = None
    ignoredTrees: Optional[List[str]] = None
    trees: List[str]

class PhotoEvent(BaseModel):
    date: str
    note: Optional[str] = None
    environments: List[str]
    _type: str
    mainTree: List[str]
    active: bool
    environmentsTrees: Dict[str, List[str]]
    type: str
    trees: List[str]
    rrule: Optional[str] = None
    id: str
    originalPath: Optional[str] = None
    timestamp: Optional[Dict[str, int]] = None
    path: HttpUrl
    source: str

class Event(BaseModel):
    reminders: Optional[List[ReminderEvent]] = None
    photos: Optional[List[PhotoEvent]] = None

class Strain(BaseModel):
    seedFinderId: Optional[str] = None
    breederId: Optional[str] = None
    strainClass: Optional[str] = None
    breederName: Optional[str] = None
    name: str
    description: Optional[str] = None
    strainId: Optional[str] = None
    avatar: Optional[HttpUrl] = None
    type: Optional[str] = None
    strainSource: Optional[str] = None
    id: Optional[str] = None

class EnvironmentInfo(BaseModel):
    name: str
    id: str
    type: Optional[str] = None

class EnvironmentMove(BaseModel):
    date: str
    pastEnvironment: EnvironmentInfo
    newEnvironment: EnvironmentInfo

class StageChange(BaseModel):
    date: str
    from_: str = Field(..., alias="from")
    to: str

class Stage(BaseModel):
    germination: Optional[str] = None
    seedling: Optional[str] = None
    rooting: Optional[str] = None
    vegetative: Optional[str] = None
    flowering: Optional[str] = None
    drying: Optional[str] = None
    curing: Optional[str] = None

class Tree(BaseModel):
    mediumDesc: Optional[str] = None
    mediumType: Optional[str] = None
    weight: Optional[str] = None
    environmentMoves: List[EnvironmentMove]
    environment: EnvironmentInfo
    strain: Optional[Strain] = None
    name: str
    avatar: Optional[Avatar] = None
    stageChanges: List[StageChange]
    stage: str
    archiveDate: Optional[str] = None
    state: str
    updatedAt: Optional[Dict[str, int]] = None
    germinatingDate: Optional[str] = None
    seedlingDate: Optional[str] = None
    rootingDate: Optional[str] = None
    vegetativeDate: Optional[str] = None
    floweringDate: Optional[str] = None
    dryingDate: Optional[str] = None
    curingDate: Optional[str] = None
    stages: Stage

class User(BaseModel):
    lengthUnit: Optional[str] = None
    temperatureUnit: Optional[str] = None

class GrowLog(BaseModel):
    age: int
    environment: Optional[Environment] = None
    events: Dict[str, Event]
    lastUpdate: str
    photosCount: int
    tree: Tree
    user: User
    views: int
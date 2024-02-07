package nl.tudelft.jpacman.level;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.mock;

import nl.tudelft.jpacman.board.Board;
import nl.tudelft.jpacman.sprite.PacManSprites;
import nl.tudelft.jpacman.npc.Ghost;
import nl.tudelft.jpacman.npc.ghost.GhostFactory;
import nl.tudelft.jpacman.points.PointCalculator;
import nl.tudelft.jpacman.points.PointCalculatorLoader;
import nl.tudelft.jpacman.board.Square;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

public class LevelFactoryTest {
    /*
     * - LevelFactory(PacManSprites, GhostFactory, PointCalculator)
     *   > Instantiations
     *     - PacManSprites
     *     - PacManSprites => GhostFactory
     *     - PointCalculatorLoader => PointCalculator
     */
    private static final PacManSprites pms = new PacManSprites();
    private final GhostFactory ghsFac = new GhostFactory(pms);
    private final PointCalculatorLoader pcl = new PointCalculatorLoader();
    private final PointCalculator pc = pcl.load();
    private final LevelFactory lvlFac = new LevelFactory(pms, ghsFac, pc);
    /*
     * - createLevel(Board, List<Ghost>, List<Square>)
     *   > Mock Board, Create Lists using ArrayList
     */
    private final Board board = mock(Board.class);
    private final List<Ghost> ghosts = new ArrayList<>();
    private final List<Square> startPositions = new ArrayList<>();

    @Test
    void testCreateLvl(){
        assertThat(lvlFac.createLevel(board, ghosts, startPositions)).isNotNull();
    }
}
